from django.urls import path
from .views import TodoList, TodoDetail, TodoCreate, TodoUpdate, \
    TodoDelete, TodoLogin, TodoRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TodoLogin.as_view(), name="login"),
    # logout and send the user to login page
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', TodoRegister.as_view(), name="register"),
    path('', TodoList.as_view(), name="list"),
    path('detail/<int:pk>/', TodoDetail.as_view(), name="detail"),
    path('create/', TodoCreate.as_view(), name="create"),
    path('update/<int:pk>', TodoUpdate.as_view(), name="update"),
    path('delete/<int:pk>', TodoDelete.as_view(), name="delete"),
]
