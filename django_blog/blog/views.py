from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
class CustomPostListView(generics.ListAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class CustomPostDetailView(generics.DetailAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class CustomPostCreateView(generics.CreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class CustomPostUpdateView(generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class CustomPostDeleteView(generics.DeleteAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class MyAPIView(APIView):
    permission = [IsAuthenticated]
    require = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        return Response({'message': 'Hello, user!'})

class CommentCreateView(generics.CreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class CommentUpdateView(generics.UpdateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class CommentDeleteView(generics.DeleteAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer
class LoginRequiredMixin
class UserPassesTestMixin
"Post.objects.filter", "title__icontains", "tags__name__icontains", "content__icontains"