from django.contrib import admin
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', BookList.as_view(), name='new boook'),
    path('api/', include(router.urls)),
]
