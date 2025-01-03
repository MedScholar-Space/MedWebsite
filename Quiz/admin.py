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

    
#admin.site.register(Quiz)
admin.site.register(Answer)



