from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy
from accounts.forms import UserRegisterForm, UserEditForm, ChangePasswordForm, ProfileEditForm
from accounts.models import Profile
from django.contrib.auth.views import PasswordChangeView

class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_user_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProfileCreateView(generic.CreateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user
    

    
class ProfileEditView(generic.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile


class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('pw_change_success')

def pw_change_success(request):
    return render(request, 'registration/pw_change_success.html', {})