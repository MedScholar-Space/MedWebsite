from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','approved']
    search_fields = ['user__username',]
    list_filter = ['approved','semestre']
from django.contrib import admin
admin.site.site_title="MedSchool"
admin.site.site_header='MedSchool'
admin.site.register(Semestre)
'''
    fieldsets = [
        (
            None,
            {
                "fields": ["user", "approved", "date_of_birth"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["semestre", "profilePic"],
            },
        ),
    ]
'''