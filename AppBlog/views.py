from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, SearchForm
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

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'

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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# class AddCommentView(CreateView, LoginRequiredMixin):
#     model = Comment
#     form_class = CommentForm
#     template_name = 


#To do Create category selection menu

class EditPostView(UpdateView, LoginRequiredMixin):
    model = Post
    template_name = 'AppBlog/edit_post.html'
    fields = ['title', 'category', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = "AppBlog/delete_post.html"
    success_url = reverse_lazy('home')

def page_not_found(request):
    return render(request, '404.html')