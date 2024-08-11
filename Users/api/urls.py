from django.urls import path
from Users.api.views import RegisterView, LoginView, LogoutView, RegisterLibrianView

app_name = 'Users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api_register'),
    path('register_librian/', RegisterLibrianView.as_view(), name='api_register_librian'),
    path('login/', LoginView.as_view(), name='api_login'),
    path('logout/', LogoutView.as_view(), name='api_logout')
]