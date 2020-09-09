from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='index'),
    path('students/<id>', views.students_detail, name='students'),
    path('scores', views.scores, name='scores')
]