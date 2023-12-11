from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Author, Reader
from .forms import PostForm, ReaderForm, AuthorForm, SearchForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def index(request):
    post = Post.objects.all()
    author = Author.objects.all()
    reader = Reader.objects.all()
    return render(request, 'index.html', {'post': post,'author': author, 'reader': reader})

def contact(request):
    context = {}
    return render(request, 'AppBlog/contact.html', context)

def about(request):
    context = {}
    return render(request, 'AppBlog/about.html', context)

def post(request):
    context = {}
    return render(request, 'AppBlog/post.html', context)

def add_author(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author = author_form.save()
            return redirect('index')
    else:
        author_form = AuthorForm()
    return render(request,'AppBlog/add_author.html',{'author_form': author_form})

def add_reader(request):
    if request.method == 'POST':
        reader_form = ReaderForm(request.POST)
        if reader_form.is_valid():
            reader = reader_form.save()
            return redirect('index')
    else:
        reader_form = ReaderForm()
    return render(request,'AppBlog/add_reader.html',{'reader_form': reader_form})

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    
class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'

class ReaderList(ListView):
    model = Reader
    template_name = 'reader_list.html'

def search_post(request):
    search_form = SearchForm(request.GET or None)
    results = Post.objects.all()
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        results = Post.objects.filter(title__icontains=query)
    return render(request, 'search_post.html', {'search_form': search_form, 'results': results})

# To do: Create funtionality, replace index and listview

class HomeView(ListView):
    model = Post
    template_name =  'AppBlog/home.html'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'AppBlog/post_detail.html'

class AddPostView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'AppBlog/add_post.html'

class EditPostView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'AppBlog/edit_post.html'
    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = "AppBlog/delete_post.html"
    success_url = reverse_lazy('home')

def page_not_found(request):
    return render(request, '404.html')