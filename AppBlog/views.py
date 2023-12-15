from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from .forms import PostForm, SearchForm, CommentForm, CategoryForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post': post})

def contact(request):
    context = {}
    return render(request, 'AppBlog/contact.html', context)

def about(request):
    context = {}
    return render(request, 'AppBlog/about.html', context)

def post(request):
    context = {}
    return render(request, 'AppBlog/post.html', context)

class CategoryList(ListView):
    model = Category
    template_name = 'AppBlog/category_list.html'

class AddCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'AppBlog/add_category.html'
    success_url = reverse_lazy('category_list')

def search_post(request):
    search_form = SearchForm(request.GET or None)
    results = Post.objects.all()
    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        results = Post.objects.filter(title__icontains=query)
    return render(request, 'search_post.html', {'search_form': search_form, 'results': results})

class HomeView(ListView):
    model = Post
    template_name = 'AppBlog/home.html'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'AppBlog/post_detail.html'

class AddPostView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'AppBlog/add_post.html'
# Function to assign user as post author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm
    template_name = 'AppBlog/add_comment.html'
# Function to assign the blog post id and user to the comment. Defines which comment belongs to which post and which user created it.
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class EditPostView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'AppBlog/edit_post.html'
    fields = ['title', 'category_name', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = "AppBlog/delete_post.html"
    success_url = reverse_lazy('home')

def page_not_found(request):
    return render(request, '404.html')