from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy
from accounts.forms import UserRegisterForm, UserEditForm, ChangePasswordForm
from django.contrib.auth.views import PasswordChangeView

class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserProfileView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('profile')

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('pw_change_success')

def pw_change_success(request):
    return render(request, 'registration/pw_change_success.html', {})