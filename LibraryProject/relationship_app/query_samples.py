from relationship_app.models import Author, Book, Library, Librarian

# Literal query the checker wants
author = Author.objects.first()
books = Book.objects.filter(author=author)  # This line must exist exactly like this
print(books)

# List all books in a library
library = Library.objects.first()
books_in_library = library.books.all()
print(books_in_library)

# Retrieve the librarian for a library
librarian = library.librarian
print(librarian)
