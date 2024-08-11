from django.urls import path
from Users.views import register, login, register_librian

app_name = 'Users'

urlpatterns = [
    path('register/', register, name='register'),
    path('register_librian/', register_librian, name='register_librian'),
    path('login/', login, name='login'),
]
