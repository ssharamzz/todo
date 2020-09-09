from . import views
from django.urls import path, include

app_name = 'second'
urlpatterns = [
    path('', views.layout, name='layout'),
    path('index', views.index, name='index'),
    path('favourite', views.favourites, name='favourites'),
    path('todo', views.todo, name='todos'),
    path('favourite/<int:id>', views.favourites_detail, name='fav_detail'),
    path('todo/<int:id>', views.todo_detail, name='todo_detail'),
    
]