from django.shortcuts import render
from .models import Book

def book_list(request):      
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'list_books': books}  # Create a context dictionary with book list
      return render(request, 'books/list_books.html', context)
