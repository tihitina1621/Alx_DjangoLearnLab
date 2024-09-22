from django.contrib import admin
from django.urls import path
from .views import PostDeleteView, PostUpdateView, PostCreateView

urlpatterns = [
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('comment/<int:pk>/update/', ),
    path( "post/<int:pk>/comments/new/",)
    path("comment/<int:pk>/delete/'),
    tags/<slug:tag_slug>/", "PostByTagListView.as_view()"
]