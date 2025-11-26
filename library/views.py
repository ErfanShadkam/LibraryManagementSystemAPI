from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Book, Author, Category
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer
from users.permissions import IsAdminOrLibrarian

class LibraryBaseViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for library models with custom permissions.
    Authenticated users can read; only admin/librarian can create/update/delete.
    """
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsAdminOrLibrarian()]
        return [IsAuthenticated()]


@extend_schema(description="Retrieve, create, update, or delete books.")
class BookViewSet(LibraryBaseViewSet):
    queryset = Book.objects.select_related('author', 'category').all()
    serializer_class = BookSerializer
    filterset_fields = ['category__id', 'author__id', 'isbn']
    search_fields = ['title', 'author__name', 'isbn']
    ordering_fields = ['title', 'price', 'quantity']


@extend_schema(description="Retrieve, create, update, or delete authors.")
class AuthorViewSet(LibraryBaseViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@extend_schema(description="Retrieve, create, update, or delete categories.")
class CategoryViewSet(LibraryBaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
