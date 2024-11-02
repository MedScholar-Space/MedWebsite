from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cours/',views.cours,name= 'cours'),
    path('cours/<str:pk>',views.course,name= 'course'),
    path('semestres/',views.semestre_categories,name='semestres'),
    path('modules/',views.test,name='modules'),
    path('',views.home,name='home'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)