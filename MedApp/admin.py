from django.contrib import admin
from django.contrib.admin import *
from .models import *
# Register your models here.

@admin.register(cour)
class CourAdmin(ModelAdmin):
    list_display = ['titre']
@admin.register(Resume)
class ResumeAdmin(ModelAdmin):
    list_display = ['titre']
@admin.register(support_cour)
class SupportAdmin(ModelAdmin):
    list_display = ['titre']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['module']
admin.site.register(Contact)