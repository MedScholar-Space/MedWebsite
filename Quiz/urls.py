from django.urls import path
from . import views



urlpatterns =[
    path('qcm/<int:pk>/',views.quiz_view    ,name='quiz_view'),
    path('qcm/',views.home,name='quiz_index'),  
    path('historique/',views.quiz_history_view,name='history'),
    path('historique/<int:pk>',views.result_id,name='history-view'),
]