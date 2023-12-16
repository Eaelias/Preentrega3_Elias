from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)
    post_date = models.DateField(auto_now_add=True)
    category_name = models.ForeignKey(Category, max_length=50, on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField (max_length=30)
    email = models.EmailField (max_length=30)
    phone_number = models.CharField(max_length=30)
    message = models.TextField (max_length=500)
