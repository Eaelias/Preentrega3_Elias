from django import forms
from .models import Post, Contact, Comment, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category_name', 'body', 'post_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category_name': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']

class SearchForm(forms.Form):
    query = forms.CharField(label='Search_Form', max_length=100)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'