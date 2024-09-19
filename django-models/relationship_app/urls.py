from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    
]