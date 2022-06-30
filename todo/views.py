from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Todo

# Create your views here.
class TodoList(ListView):
    model = Todo
    context_object_name = 'tasks'

class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'task'

class TodoCreate(CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')