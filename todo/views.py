from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# restrict the views so that they can only be seen if logged in
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Todo


# Login page
class TodoLogin(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')


# Register page
class TodoRegister(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list')

    # making sure user is logged in and redirected
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TodoRegister, self).form_valid(form)

    # blocking registered user from seeing the register page again
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(TodoRegister, self).get(*args, **kwargs)


# Main page list view
class TodoList(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'tasks'

    # modified method from django documentation
    # ensuring that users can get their own lists
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context


# Details page
class TodoDetail(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'task'


# Create task page
class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('list')

    # override method so that the correct user is
    # selected and new task can be added for it
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)


# Update task page
class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('list')


# Delete task page
class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('list')
