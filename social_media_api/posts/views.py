from django.shortcuts import render
#from rest_framework import viewsets, permissions 
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def follow(request):
    following_user = request.user.follows.all()
    posts = Post.objects.filter(author__in=following_users).order_by('created_at')
    permission_classes = [permissions.IsAuthenticated]
    return (following.all(), posts, following_user, permission_classes)
