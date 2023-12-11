"""
URL configuration for AppBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppBlog.views import contact, about, post, add_author, add_reader, search_post, PostList, ReaderList, AuthorList, AddPostView, HomeView, PostDetailView, EditPostView, DeletePostView

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('add_author/', add_author, name='add_author'),
    path('add_reader/', add_reader, name='add_reader'),
    path('post_list', PostList.as_view(), name='post_list'),
    path('author_list', AuthorList.as_view(), name='author_list'),
    path('reader_list', ReaderList.as_view(), name='reader_list'),
    path('search_post', search_post, name='search_post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('home', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]
