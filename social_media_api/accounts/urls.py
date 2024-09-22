from django.contrib import admin
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('register/', admin.site.urls),
    path('login/', BookList.as_view(), name='new boook'),
    path('api/', include(router.urls)),
    path('unfollow/<int:user_id>/', ),
    path('follow/<int:user_id>'),
]