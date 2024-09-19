from django.db import models
from . import User

class Author(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library)
Admin = ['Librarian', 'Member']
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=50, choices=Admin)

