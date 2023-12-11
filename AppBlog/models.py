from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    #post_id = models.IntegerField(unique=True) # Check id pk functionality
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
    

class Author(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()

class Reader(models.Model):
    username = models.CharField(max_length=20)
    user_id = models.IntegerField(unique=True)
    email = models.EmailField()

class Contact(models.Model):
    name = models.CharField (max_length=30)
    email = models.EmailField (max_length=30)
    phone_number = models.CharField(max_length=30)
    message = models.TextField (max_length=500)
