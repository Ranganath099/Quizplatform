from django.contrib import admin
from .models import Quiz, Question, Choice, QuizAttempt

#Register models in admin  can have acces on the models

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'attempted_at','correct_answers')
    ordering = ('-score', 'correct_answers')  # Show highest scores first
    list_filter = ('quiz', 'attempted_at')
    search_fields = ('user__username', 'quiz__title')

    def get_queryset(self, request):
        """Limit the leaderboard display to the top 10 highest scores."""
        queryset = super().get_queryset(request)
        return queryset.order_by('-score')

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizAttempt,  QuizAttemptAdmin)