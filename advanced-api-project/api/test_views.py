from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User

from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user and author
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="George Orwell")

        # Auth client for create/update/delete
        self.auth_client = APIClient()
        self.auth_client.login(username='testuser', password='password123')

        # Book for testing retrieve/update/delete
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }
        response = self.auth_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "Brave New World",
            "publication_year": 1932,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {"title": "Nineteen Eighty-Four", "publication_year": 1949, "author": self.author.id}
        response = self.auth_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.auth_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=1984'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_search_books_by_author_name(self):
        url = reverse('book-list') + '?search=Orwell'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['author'], self.author.id)

    def test_order_books_by_title(self):
        Book.objects.create(title="A Tale of Two Cities", publication_year=1859, author=self.author)
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))
