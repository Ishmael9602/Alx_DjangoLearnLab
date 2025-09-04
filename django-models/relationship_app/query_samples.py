import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author using ForeignKey relationship
    """
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        
        print(f"Books by {author_name}:")
        for book in books:
            print(f"  - {book.title}")
        
        return books
    
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_books_in_library(library_name):
    """
    List all books in a library using ManyToMany relationship
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"Books in {library_name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")
        
        return books
    
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library using OneToOne relationship
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        
        print(f"Librarian for {library_name}: {librarian.name}")
        return librarian
    
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


if __name__ == "__main__":
    # Create sample data for testing
    author1 = Author.objects.get_or_create(name="J.K. Rowling")[0]
    author2 = Author.objects.get_or_create(name="George Orwell")[0]
    
    book1 = Book.objects.get_or_create(title="Harry Potter", author=author1)[0]
    book2 = Book.objects.get_or_create(title="1984", author=author2)[0]
    
    library1 = Library.objects.get_or_create(name="Central Library")[0]
    library1.books.add(book1, book2)
    
    librarian1 = Librarian.objects.get_or_create(name="Alice Johnson", library=library1)[0]
    
    # Test the queries
    print("=== Testing Relationships ===")
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    retrieve_librarian_for_library("Central Library")
