from django.db import models
from Quiz.models import *
from django.contrib.auth.models import User
# Create your models here.
import random

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(help_text="questions correct")
    resultat = models.IntegerField(null=True)
    date_taken = models.DateTimeField(auto_now_add=True)
    def get_random_color(self):
        colors = ['bg-danger', 'bg-warning', 'bg-success', 'bg-info','bg-secondary','bg-dark','bg-primary']
        return random.choice(colors)
    class Meta:
        ordering = ('-date_taken',)
'''    def __str__(self):
        return f"{self.user.username} - {self.quiz.name} - {self.score}"
'''

class QuestionResult(models.Model):
    result = models.ForeignKey(Result, related_name='question_results', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    explication = models.TextField()
    selected_answers = models.ManyToManyField(Answer, related_name='selected_by_results')
    correct_answers = models.ManyToManyField(Answer, related_name='correct_for_results')
    is_correct = models.BooleanField()

