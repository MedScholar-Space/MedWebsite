from django.contrib import admin
from .models import *
# Register your models here.
class QuestionRAdmin(admin.StackedInline):
    model = QuestionResult
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    inlines=[QuestionRAdmin]
    