from django.db import models
import random
from MedApp.models import Category 
# Create your models here.
from dashboard.models import Semestre


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    categorie = models.ForeignKey(Category,models.CASCADE)
    semestre= models.ForeignKey(Semestre,models.CASCADE)
    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    image= models.ImageField(upload_to="Quiz_Images/",blank=True,null=True)
    text = models.CharField(max_length=255)
    explication = models.TextField()
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    
class Comment(models.Model):
    Quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    Your_Name = models.CharField(max_length=80,)
    Your_Email = models.EmailField()
    Your_Comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return f'Comment by {self.Your_Name} on {self.Quiz}'


