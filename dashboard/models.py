from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Semestre(models.Model):
    Background_Choices=[
    ('','blue'),
    ('card__orange','orange'),
    ('card__green','green')
    ]
    semestre = models.CharField(max_length=200,help_text="Niveau ou Semestre où les étudiants étudie.")
    background=models.TextField(choices=Background_Choices,max_length=200,null=True,blank=True)
    icon = models.CharField(max_length=200,default='ri-flashlight-line')
    Gif_icon = models.FileField(upload_to="gif_icons",default=None,blank=True,null=True)
    def __str__(self):
        return self.semestre
class Profile(models.Model):
    user = models.OneToOneField(User,models.CASCADE,help_text='User linked to this profile')
    profilePic = models.FileField(upload_to='Profile-pic', blank=True, null=True,help_text='Profile picture')
    date_of_birth = models.DateField(blank=True, null=True,help_text='Birth Day')
    approved = models.BooleanField(default=True, help_text='Is the profile is approved')
    semestre = models.ManyToManyField(Semestre,help_text="hold the ctrl key and select all the available choices")
    def __str__(self):
        return str(self.user.email)
