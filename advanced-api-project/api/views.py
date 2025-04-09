from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



#  List all books
class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of all books in the database.

    - Method: GET
    - Permissions: Public access allowed
    - Returns: JSON list of book objects
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.AllowAny]
    permission_classes = [AllowAny]


#  Retrieve one book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by its primary key (ID).

    - Method: GET
    - Permissions: Public access allowed
    - Returns: JSON object of the specified book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    # permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filtering
    filterset_fields = ['title', 'author', 'publication_year']
    
    # Searching (partial matches)
    search_fields = ['title', 'author__name']
    
    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering



# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book instance.

    - Method: POST
    - Permissions: Authenticated users only
    - Validates: `title`, `publication_year`, and `author`
    - Returns: Created book object
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]


#  Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update details of an existing book.

    - Method: PUT or PATCH
    - Permissions: Authenticated users only
    - URL Param: Book ID
    - Returns: Updated book object
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book from the database.

    - Method: DELETE
    - Permissions: Authenticated users only
    - URL Param: Book ID
    - Returns: 204 No Content on success
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]
