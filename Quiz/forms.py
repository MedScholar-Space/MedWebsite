# quiz/forms.py
from django import forms
from django.forms import ModelForm
from .models import Question, Answer, Comment


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super().__init__(*args, **kwargs)

        if questions:
            for question in questions:
                # Get answer choices for this question
                answers = question.answers.all()
                
                # Create a multiple choice field for each question
                self.fields[f'question_{question.id}'] = forms.MultipleChoiceField(
                    choices=[ (answer.id,answer.text)  for answer in answers],
                    widget=forms.CheckboxSelectMultiple,
                    required=False,
                    label=question.text
                )
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('Your_Name', 'Your_Email', 'Your_Comment')
        widgets = {
            'Your_Name': forms.TextInput(attrs={'placeholder': 'Enter Your Name','class':'form-control'}),
            'Your_Email':forms.EmailInput(attrs={'placeholder':'Enter your email adress please','class':'form-control'}),
            'Your_Comment': forms.Textarea(
                attrs={'placeholder': 'Enter Your comments here','class':'form-control'}),
        }
