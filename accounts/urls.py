from django.urls import path
from accounts.views import UserRegisterView, UserEditView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('edit_profile/', UserEditView.as_view(template_name="registration/edit_profile.html"), name='edit_profile'),
]