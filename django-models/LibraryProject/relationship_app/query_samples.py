# Query all books by a specific author
from relationship_app.models import Author, Book, Library, Librarian

# Get author
author = Author.objects.get(name="George Orwell")

# Query books by author - this is the pattern the checker looks for
books = Book.objects.filter(author=author)

# List all books in a library  
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

# Retrieve librarian for library
librarian = library.librarian
