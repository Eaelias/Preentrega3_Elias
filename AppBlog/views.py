from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppBlog.forms import ContactForm
from AppBlog.models import Contact

def show_html(request):
    context = {}
    return render(request, 'index.html', context)

def contact(request):
    # if request.method == "POST":
    #     Contact_form = ContactForm(request.POST)
    #     if Contact_form.is_valid():
    #         information = ContactForm.cleaned_data

    #         create_contact = Contact(name=information.name, email=information.email, phone_number=information.phone_number, message=information.message)
    #         Contact_form.save()
    #         return redirect("/BlogApp/")
    # ContactForm = Contact()
    context = {
        "form": ContactForm()
    }
    return render(request, 'AppBlog/contact.html', context)