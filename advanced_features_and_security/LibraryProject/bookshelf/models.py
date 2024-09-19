from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=70)
    publication_year = models.IntegerField()
class AbstractUser(models.Model):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    