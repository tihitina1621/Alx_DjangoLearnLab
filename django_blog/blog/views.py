from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
class CustomPostListView(generics.ListAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomPostDetailView(generics.DetailAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomPostCreateView(generics.CreateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomPostUpdateView(generics.UpdateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomPostDeleteView(generics.DeleteAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class MyAPIView(APIView):
    permission = [IsAuthenticated]
    require = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        return Response({'message': 'Hello, user!'})

