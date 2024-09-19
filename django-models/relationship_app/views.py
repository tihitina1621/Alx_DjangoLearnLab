from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView

def book_list(request):      
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)
  
class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'
def get_context_data(self, **kwargs):    
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating() 
def index(request):
    return render(request, 'library_detail.html')
