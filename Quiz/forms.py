# quiz/forms.py
from django import forms
from .models import Question, Answer

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        iteration=1

        for question in questions:
            image_tag = f'<img src="{question.image.url}" alt="{question.text}" class="img-thumbnail" style="width:200px;height:200px" />' if question.image else ''
            label_with_image = f'{iteration} - {question.text} <br> {image_tag} '
            self.fields[f'question_{question.id}'] = forms.ModelMultipleChoiceField(
                queryset=question.answers.all(),
                widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox form-check-input'}),
                required=False,
                label=label_with_image,
            )
            iteration += 1