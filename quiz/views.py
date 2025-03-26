from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Quiz, QuizAttempt, Question, Choice
from .forms import QuizForm, QuestionForm, ChoiceForm
from django.contrib import messages \
 

@login_required
def exam_list(request):
    quizzes = Quiz.objects.all()
    leaderboard = QuizAttempt.objects.order_by('-score')[:10]
    return render(request, 'exam_list.html', {'quizzes': quizzes, 'leaderboard':leaderboard})

def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'take_quiz.html', {'quiz': quiz})

def leaderboard(request):
    attempts = QuizAttempt.objects.order_by('-score')[:10]
    return render(request, 'leaderboard.html', {'attempts': attempts})

def is_examiner(user):
    return user.is_staff  # Only staff users (examiners) can create quizzes

@login_required
@user_passes_test(is_examiner)
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            return redirect('add_question', quiz_id=quiz.id)  # Redirect to add questions
    else:
        form = QuizForm()
    return render(request, 'create_quiz.html', {'form': form})


@login_required
@user_passes_test(is_examiner)
def add_question(request, quiz_id):
    """Allow examiners to add multiple questions to a quiz."""
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save()
            return redirect('add_question', quiz_id=quiz.id)  # Stay on the same page to add more questions

    else:
        form = QuestionForm()

    return render(request, 'add_question.html', {'form': form, 'quiz': quiz, 'questions': quiz.questions.all()})
@login_required
@user_passes_test(is_examiner)
def delete_question(request, question_id):
    """Allow examiners to delete a question."""
    question = get_object_or_404(Question, id=question_id)
    quiz_id = question.quiz.id
    question.delete()
    return redirect('add_question', quiz_id=quiz_id)


@login_required
@user_passes_test(is_examiner)
def add_choices(request, question_id):
    """Allow examiners to add multiple choices to a question."""
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('add_choices', question_id=question.id)  # Stay on the page to add more choices

    else:
        form = ChoiceForm()

    return render(request, 'add_choices.html', {'form': form, 'question': question, 'choices': question.choices.all()})

@login_required
@user_passes_test(is_examiner)
def delete_choice(request, choice_id):
    """Allow examiners to delete a choice."""
    choice = get_object_or_404(Choice, id=choice_id)
    question_id = choice.question.id
    choice.delete()
    return redirect('add_choices', question_id=question_id)


@login_required
@user_passes_test(is_examiner)
def delete_quiz(request, quiz_id):
    """Allow examiners to delete a quiz."""
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_list')  # Redirect to quiz list after deletion

    return render(request, 'delete_quiz.html', {'quiz': quiz})
@login_required
@user_passes_test(is_examiner)
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

@login_required
@user_passes_test(is_examiner)
def view_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'view_quiz.html', {'quiz': quiz})


@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    score = 0
    correct_answers = 0  # Track correct answers separately

    for question in quiz.questions.all():
        selected_choice_id = request.POST.get(str(question.id))
        
        if selected_choice_id:
            choice = Choice.objects.filter(id=selected_choice_id).first()  # Avoid exception
            if choice and choice.is_correct:
                correct_answers += 1  # Count correct answers
                score += 1  # Adjust score logic if needed (e.g., 10 points per correct answer)

    # Save the attempt
    QuizAttempt.objects.create(user=request.user,quiz=quiz,score=score,correct_answers=correct_answers)  # Save correct answer count


    return redirect('leaderboard')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('exam_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)# Custom role-based redirection
            if  user.is_staff:  
                return redirect('quiz_list')
            else:
                return redirect('exam_list')# Default redirect for other users

        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('exam_list')