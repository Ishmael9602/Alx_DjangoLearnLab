from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# List all books (view requires can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Example form view
@permission_required('bookshelf.can_create', raise_exception=True)
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Here you can handle form data safely
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # For demonstration, we won't save it to the database
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
