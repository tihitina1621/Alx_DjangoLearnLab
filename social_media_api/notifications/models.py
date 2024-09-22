from django.db import models
from .models import User
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    verb = models.TextField()
    target = GenericForeignKey()
    timestamp = models.DateTimeField()