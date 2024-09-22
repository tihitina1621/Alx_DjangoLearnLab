from django.contrib import admin
from django.urls import path
from .views import PostDeleteView, PostUpdateView, PostCreateView

urlpatterns = [
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]