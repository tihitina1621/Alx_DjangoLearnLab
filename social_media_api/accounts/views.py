from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser, Post
class ULV(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

   
def follow(request):
    following_user = request.user.follows.all()
    posts = Post.objects.filter(author__in=following_users).order_by('created_at')
    permission_classes = [permissions.IsAuthenticated]
    return (following.all(), posts, following_user, permission_classes)
def
return Response