from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html")), name='logout'),
    path('', views.register),
    path('manage-books/', views.manage_books, name='manage_books'),
]