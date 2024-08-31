from django.db import models

class BooK(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
