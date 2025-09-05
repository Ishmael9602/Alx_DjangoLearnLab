from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library

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
