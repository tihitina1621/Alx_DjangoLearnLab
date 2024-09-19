from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('library/<int:pk>/', list_books.as_view(), name='library-detail'),
]