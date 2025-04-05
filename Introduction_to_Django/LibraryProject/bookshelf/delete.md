# Delete the book.
book.delete()

# Confirm deletion by retrieving all books.
books = Book.objects.all()
print(books) 

# outcome
<QuerySet []>