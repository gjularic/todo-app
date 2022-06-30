from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Todo

# Create your views here.
class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'