from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    post_id = forms.IntegerField()

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    message = forms.TextInput()
