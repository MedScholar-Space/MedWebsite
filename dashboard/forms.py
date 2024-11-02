from django import forms
from django.contrib.auth.models import User
from .models import Profile
import datetime
from django.forms.widgets import *
from django.contrib.auth.models import User as user
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

def request(request):
    profile = request.user.profile
    return profile

class LoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Please Enter your password"}))
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Répéter le mot de passe  ',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',)
        widgets={
            'date_of_birth':SelectDateWidget(years=range(1900,3000),empty_label=("Choose Year", "Choose Month", "Choose Day"))
        }  
class ImageEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilePic',)

class ProfileRegistration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',)
        widgets={
        'date_of_birth':SelectDateWidget(years=range(1900,3000),attrs={'class':'select'},empty_label=("Choose Year", "Choose Month", "Choose Day")),
        }