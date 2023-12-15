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
from AppBlog.views import contact, about, post, search_post, HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, AddCommentView, CategoryList, AddCategory


urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('add_category', AddCategory.as_view(), name='add_category'),
    path('category_list', CategoryList.as_view(), name='category_list'),
    path('search_post', search_post, name='search_post'),
]
