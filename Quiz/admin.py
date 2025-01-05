from django.contrib import admin
import nested_admin

# Register your models here.
from .models import *
# Register your models here.


'''
class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1  # Number of blank forms for new answers

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1  # Number of blank forms for new questions

    # Override the get_formset method to include Answer inlines manually
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:
            for question in obj.questions.all():
                # Include answers manually here
                admin.site._registry[Answer].get_formset(request, obj=question, **kwargs)
        return formset

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
'''    
from django.contrib import admin
import nested_admin

# Register your models here.
from .models import *
# Register your models here.



class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer



class QuestionAdmin(nested_admin.NestedStackedInline):
    inlines = [AnswerInline]
    model = Question
@admin.register(Quiz)
class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines= [QuestionAdmin]

    
admin.site.register(Answer)
