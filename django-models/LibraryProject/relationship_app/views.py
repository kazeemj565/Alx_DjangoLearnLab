# from django.shortcuts import render, get_object_or_404
# from .models import Book, Library
# from django.views.generic import DetailView

# # Function-based view to list all books.
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'list_books.html', {'books': books})


# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'library_detail.html'
#     context_object_name = 'library'



# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view to list all books.
def list_books(request):
    books = Book.objects.all()
    # Explicitly reference the template within the relationship_app folder.
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
