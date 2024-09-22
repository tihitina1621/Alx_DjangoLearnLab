from django.urls import path
from . import views

urlpattrns  = [
    path('feel/', views.feed_endpoint, name='feed_endpoint',)
]