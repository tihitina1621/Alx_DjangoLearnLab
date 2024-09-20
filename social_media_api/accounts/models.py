from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomUser(AbstractUser):
    bio = models.CharField(max_length=200)
    profile_picture = models.ImageField()
    followers = models.ManyToManyField(CustomUser, symmetrical=False)