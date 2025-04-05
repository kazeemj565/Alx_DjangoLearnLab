from bookshelf.models import Book

# Create a Book instance with title, author, and publication year.
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  

# outcome
1984 by George Orwell





