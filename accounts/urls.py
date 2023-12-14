from django.urls import path
from accounts.views import UserRegisterView, UserEditView, UserProfileView, PasswordsChangeView
from django.contrib.auth.views import LogoutView
from .views import pw_change_success

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('<int:pk>/profile/', UserProfileView.as_view(template_name="registration/profile.html"), name='profile'),
    path('<int:pk>/edit_profile/', UserEditView.as_view(template_name="registration/edit_profile.html"), name='edit_profile'),
    path('<int:pk>/password/', PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    path('/password_change_success', pw_change_success, name="pw_change_success"),
]