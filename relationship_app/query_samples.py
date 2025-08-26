# relationship_app/query_samples.py
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Sample data
authors_data = ["J.K. Rowling", "George R.R. Martin", "J.R.R. Tolkien"]
libraries_data = ["Central Library", "Community Library"]
librarians_data = ["Mary Smith", "John Doe"]

books_data = {
    "J.K. Rowling": [
        "Harry Potter and the Sorcerer's Stone",
        "Harry Potter and the Chamber of Secrets"
    ],
    "George R.R. Martin": [
        "A Game of Thrones",
        "A Clash of Kings"
    ],
    "J.R.R. Tolkien": [
        "The Hobbit",
        "The Lord of the Rings"
    ]
}

# Create authors
authors = {}
for name in authors_data:
    author, _ = Author.objects.get_or_create(name=name)
    authors[name] = author
    print(f"Author created/found: {author.name}")

# Create libraries
libraries = {}
for name in libraries_data:
    library, _ = Library.objects.get_or_create(name=name)
    libraries[name] = library
    print(f"Library created/found: {library.name}")

# Create librarians (one per library)
for lib_name, librarian_name in zip(libraries_data, librarians_data):
    librarian, _ = Librarian.objects.get_or_create(name=librarian_name, library=libraries[lib_name])
    print(f"Librarian: {librarian.name} works at {lib_name}")

# Create books and link to libraries
for author_name, titles in books_data.items():
    author = authors[author_name]
    for title in titles:
        book, created = Book.objects.get_or_create(title=title, author=author)
        # Add all libraries to the book
        for library in libraries.values():
            book.libraries.add(library)
        if created:
            print(f"Book created: {book.title} by {author.name}")

# Display books by author
for author in authors.values():
    books_by_author = Book.objects.filter(author=author)
    if books_by_author.exists():
        print(f"Books by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"No books found for {author.name}")

# Display books in each library
for library in libraries.values():
    books_in_library = Book.objects.filter(libraries=library)
    if books_in_library.exists():
        print(f"Books in {library.name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    else:
        print(f"No books found in {library.name}")
