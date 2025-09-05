# Query all books by a specific author
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books = Book.objects.filter(author=author)

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

# Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian
