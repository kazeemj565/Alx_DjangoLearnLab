>>> from bookshelf.models import Book
 instance with title, author, and publication year>>> 

>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book) 
1984 by George Orwell


>>> books = Book.objects.all()
>>> print(books) 

<QuerySet [<Book: 1984 by George Orwell>]>

>>> book.title = "Nineteen Eighty-Four"
>>> book.save()

>>> print(book) 
Nineteen Eighty-Four by George Orwell

>>> book.delete()
books = Book.objects.all()
print(books)
(1, {'bookshelf.Book': 1})
>>> 

>>> books = Book.objects.all()
>>> print(books)
<QuerySet []>
>>> 




