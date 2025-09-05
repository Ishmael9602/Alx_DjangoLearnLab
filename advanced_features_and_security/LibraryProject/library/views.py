from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from library.models import Book

@permission_required('library.can_view', raise_exception=True)
def view_books(request):
    books = list(Book.objects.values())
    return JsonResponse({"books": books})

@permission_required('library.can_create', raise_exception=True)
def create_book(request):
    # Example JSON request
    import json
    data = json.loads(request.body)
    book = Book.objects.create(
        title=data["title"],
        author=data["author"],
        published_date=data["published_date"]
    )
    return JsonResponse({"message": "Book created", "book": {"title": book.title}})
