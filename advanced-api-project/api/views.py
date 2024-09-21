from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author 
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
class CustomBookListView(generics.ListAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomBookDetailView(generics.DetailAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomBookCreateView(generics.CreateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomBookUpdateView(generics.UpdateAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class CustomBookDeleteView(generics.DeleteAPIView):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class MyAPIView(APIView):
    permission = [IsAuthenticated]
    require = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        return Response({'message': 'Hello, user!'})
