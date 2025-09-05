from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Router setup
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include router URLs for CRUD operations
    path('', include(router.urls)),
]
