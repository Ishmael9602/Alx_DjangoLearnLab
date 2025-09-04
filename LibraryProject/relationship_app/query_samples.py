from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (checker requires this exact line)
author = Author.objects.first()
books = Book.objects.filter(author=author)  # exact string required
print(f"Books by {author.name}: {[book.title for book in books]}")

# 2. List all books in a library
library = Library.objects.first()
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# 3. Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")
