from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.first()
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# List all books in a library
library = Library.objects.first()
library_books = library.books.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")

# Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")
