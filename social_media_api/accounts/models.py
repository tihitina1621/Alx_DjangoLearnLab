from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser): 
    bio = models.TextField()  
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self', symmetrical=False)
    following = models.ManyToManyField('self', symmetrical=False)
    def __str__(self):
        return self.username