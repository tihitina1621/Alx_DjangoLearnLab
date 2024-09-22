from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignObject(User)
    content = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()

