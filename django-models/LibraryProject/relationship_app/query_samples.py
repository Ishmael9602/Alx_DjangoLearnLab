# Query samples for Django model relationships
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (ForeignKey relationship)
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# List all books in a library (ManyToMany relationship)  
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Retrieve the librarian for a library (OneToOne relationship)
library = Library.objects.get(name="Central Library")  
librarian = library.librarian
