from django.urls import path
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('todo_list'), name='home'),
    path('todo/', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('toggle/<int:pk>/', views.toggle_todo, name='toggle_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]