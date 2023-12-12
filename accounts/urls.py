from django.urls import path
from accounts.views import UserRegisterForm
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', UserRegisterForm.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('profile/', LogoutView.as_view(template_name="registration/profile.html"), name='logout'),
]