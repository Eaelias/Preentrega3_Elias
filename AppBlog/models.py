from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=80)
    post_id = models.IntegerField(unique=True)

class Author(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
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
