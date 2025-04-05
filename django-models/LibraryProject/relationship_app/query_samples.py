# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author (e.g., "George Orwell")
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# Query 2: List all books in a specific library (e.g., "Central Library")
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query 3: Retrieve the librarian for a specific library (e.g., "Central Library")
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
