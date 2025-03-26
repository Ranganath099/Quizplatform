from django.urls import path
from . import views

# Create a url path for the redireccting and rendering the pages.

urlpatterns = [
    path('quiz_list/', views.quiz_list,name='quiz_list'),
    path('', views.exam_list, name='exam_list'),
    path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/add_question/', views.add_question, name='add_question'),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path('question/<int:question_id>/add-choices/', views.add_choices, name='add_choices'),
    path('choice/<int:choice_id>/delete/', views.delete_choice, name='delete_choice'),
    path('quiz/<int:quiz_id>/delete/', views.delete_quiz, name='delete_quiz'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
