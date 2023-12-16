from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=10000)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")

    def get_absolute_url(self):
        return reverse('profile', args=(str(self.id)))
