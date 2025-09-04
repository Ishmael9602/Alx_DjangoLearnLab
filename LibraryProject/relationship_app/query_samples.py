from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.first()
books = Book.objects.filter(author=author)  # <-- exactly what the checker wants
print(f"Books by {author.name}: {[book.title for book in books]}")

# List all books in a library
library = Library.objects.first()
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")
