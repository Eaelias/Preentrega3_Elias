from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=80)
    post_id = models.IntegerField(unique=True)

class Author(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class reader(models.Model):
    username = models.CharField(max_length=20)
    user_id = models.IntegerField(unique=True)
    email = models.EmailField()

