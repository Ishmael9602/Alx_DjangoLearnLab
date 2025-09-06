from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from bookshelf.models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create some books for testing
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2001)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2002)
        self.book3 = Book.objects.create(title="Another Book", author="Author A", publication_year=2003)

        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        # Login before creating
        login = self.client.login(username="testuser", password="testpass")
        self.assertTrue(login)

        url = reverse('book-create')
        data = {"title": "New Book", "author": "New Author", "publication_year": 2020}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.latest('id').title, "New Book")

    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author=Author A'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertEqual(book['author'], 'Author A')

    def test_search_books(self):
        url = reverse('book-list') + '?search=Another'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Another" in book['title'] for book in response.data))

    def test_order_books_by_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
