from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, CategoryViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

