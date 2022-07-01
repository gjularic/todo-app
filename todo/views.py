from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Todo

# Create your views here.
class TodoLogin(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')

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

class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')
