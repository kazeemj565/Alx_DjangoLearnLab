# Retrieve all Book instances.
<!-- books = Book.objects.all() -->
print(books)

book = Book.objects.get(title="1984")
print(book.title)       
print(book.author)           
print(book.publication_year)
# outcome
<QuerySet [<Book: 1984 by George Orwell>]>