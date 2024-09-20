from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser, Post
class ULV(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

   
def follow(request):
    following_user = request.user.follows.all()
    posts = Post.objects.filter(author__in=following_users).order_by('created_at')
    return (following_user, posts)