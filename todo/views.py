from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# restrict the views so that they can only be seen if logged in
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo

# Create your views here.
class TodoLogin(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')

class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'tasks'

    # modified method from django documentation
    # ensuring that users can get their own lists
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'task'

class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')

    # override method so that the correct user is
    # selected and new task can be added for it
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')
