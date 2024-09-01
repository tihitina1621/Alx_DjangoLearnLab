from django.shortcuts import render
from rest_framework import generics, viewsets 
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BoolViewSet(viewsets.ModelViewset):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
