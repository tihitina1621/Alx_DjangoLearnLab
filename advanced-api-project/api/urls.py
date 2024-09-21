from django.urls import path
from . import views
urlpatters = [
    path('api.urls', '),
    path('books/<int:pk>', views.book_list, name = 'book_list'),
    path('books/create', views.book_create, name='book_create'),
    path('books/update<int:id>', views.book_update, name='book_update'),
    path('books/delete<int:id>', views.book_delete, name = 'book_delete')
]