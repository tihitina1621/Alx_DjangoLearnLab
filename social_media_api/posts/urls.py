from django.urls import path
from . import views

urlpattrns  = [
    path('feed/', views.feed_endpoint, name='feed_endpoint',),
    path("<int:pk>/like/"),
    path("<int:pk>/unlike/")
]