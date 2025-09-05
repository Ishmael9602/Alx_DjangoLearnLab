from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Book

@csrf_protect
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'bookshelf/form_example.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
