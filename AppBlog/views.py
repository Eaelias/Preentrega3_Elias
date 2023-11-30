from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Author
from .forms import PostForm

def index(request):
    post = Post.objects.all()
    author = Author.objects.all()
    return render(request, 'index.html', {'post': post,'author': author})

def contact(request):
    context = {}
    return render(request, 'AppBlog/contact.html', context)

def about(request):
    context = {}
    return render(request, 'AppBlog/about.html', context)

def post(request):
    context = {}
    return render(request, 'AppBlog/post.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request,'AppBlog/create_post.html',{'form': form})

def page_not_found(request):
    return render(request, '404.html')