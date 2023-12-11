from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import UserRegisterForm

# Create your views here.
def login_request(request):
    form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context) 

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save
            return redirect("index")
    form = UserRegisterForm()
    context = {
        "form":form
    }
    return render(request, "accounts/register.html", context)