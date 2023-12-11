from django import forms
from .models import Post, Author, Reader, Contact

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

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
