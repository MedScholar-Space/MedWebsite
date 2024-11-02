from django.db import models
import random
from MedApp.models import Category ,SubCategory
# Create your models here.
from dashboard.models import Semestre


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    categorie = models.ForeignKey(Category,models.CASCADE)
    sub_categorie = models.ForeignKey(SubCategory,models.CASCADE)
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
