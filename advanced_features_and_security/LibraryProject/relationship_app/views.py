from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book, Library, Author

# Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    Renders a simple list of book titles and their authors.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User registration view
def register(request):
    """
    Handle user registration using Django's UserCreationForm
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role checking functions
def check_role(user, role):
    """Helper function to check if user has a specific role"""
    return hasattr(user, 'userprofile') and user.userprofile.role == role

# Admin role check
def admin_required(user):
    return check_role(user, 'Admin')

# Librarian role check  
def librarian_required(user):
    return check_role(user, 'Librarian')

# Member role check
def member_required(user):
    return check_role(user, 'Member')

# Role-based views
@user_passes_test(admin_required)
def admin_view(request):
    """
    Admin view accessible only to users with Admin role
    """
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(librarian_required)
def librarian_view(request):
    """
    Librarian view accessible only to users with Librarian role
    """
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(member_required)
def member_view(request):
    """
    Member view accessible only to users with Member role
    """
    return render(request, 'relationship_app/member_view.html')

# Custom Permission Views for Book CRUD operations
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View to add a new book - requires can_add_book permission
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            author = get_object_or_404(Author, id=author_id)
            Book.objects.create(title=title, author=author)
            return redirect('list_books')
    
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """
    View to edit an existing book - requires can_change_book permission
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            author = get_object_or_404(Author, id=author_id)
            book.title = title
            book.author = author
            book.save()
            return redirect('list_books')
    
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """
    View to delete a book - requires can_delete_book permission
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})
