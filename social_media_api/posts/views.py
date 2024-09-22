from django.shortcuts import render
#from rest_framework import viewsets, permissions 
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import generics.get_object_or_404

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

def like(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, creat = Like.objects.get_or_create(user=request.user, post=post)
    if creat:
        Notification.objects.create(
            user=post.author,
            message=f"{request.user.username} liked your post."
        )
        message = "Liked"
    else:
        like.delete()
        Notification.objects.create(
            user=post.author,
            message=f"{request.user.username} unliked your post."
        )
        message = "Unliked"
