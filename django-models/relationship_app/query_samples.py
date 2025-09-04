import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author using filter method
def query_books_by_author():
    """
    Query all books by a specific author using objects.filter(author=author)
    """
    # Get a specific author
    author = Author.objects.get(name="J.K. Rowling")
    
    # Query all books by this author using the required pattern
    books = Book.objects.filter(author=author)
    
    print(f"Books by {author.name}:")
    for book in books:
        print(f"  - {book.title}")
    
    return books


# List all books in a library using ManyToMany relationship
def list_books_in_library():
    """
    List all books in a library using ManyToMany relationship
    """
    library = Library.objects.get(name="Central Library")
    books = library.books.all()
    
    print(f"Books in {library.name}:")
    for book in books:
        print(f"  - {book.title} by {book.author.name}")
    
    return books


# Retrieve the librarian for a library using OneToOne relationship
def retrieve_librarian_for_library():
    """
    Retrieve the librarian for a library using OneToOne relationship
    """
    library = Library.objects.get(name="Central Library")
    librarian = library.librarian
    
    print(f"Librarian for {library.name}: {librarian.name}")
    return librarian


def create_sample_data():
    """
    Create sample data for testing
    """
    # Create authors
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    
    # Create books
    book1, created = Book.objects.get_or_create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2, created = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3, created = Book.objects.get_or_create(title="1984", author=author2)
    
    # Create library
    library, created = Library.objects.get_or_create(name="Central Library")
    library.books.add(book1, book2, book3)
    
    # Create librarian
    librarian, created = Librarian.objects.get_or_create(name="Alice Johnson", library=library)


if __name__ == "__main__":
    create_sample_data()
    
    print("=== Query Books by Author (using objects.filter(author=author)) ===")
    query_books_by_author()
    
    print("\n=== List Books in Library (ManyToMany) ===")
    list_books_in_library()
    
    print("\n=== Retrieve Librarian for Library (OneToOne) ===")
    retrieve_librarian_for_library()
