from django import forms
from .models import Post, Author, Reader, Contact

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_id', 'post_text']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'lastname', 'email']

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['username', 'user_id', 'email']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search_Form', max_length=100)