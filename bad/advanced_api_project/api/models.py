from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.TimeField()
    author = models.ForeignKey(Author)
#Two models are defiend with foreignkey which will enable the two models to have a one to one relationship.