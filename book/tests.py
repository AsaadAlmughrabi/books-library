from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book

class ViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        
        self.book = Book.objects.create(
            title="Test Book",
            description="Test Description",
            rating=5,
            publish_date="2024-07-17",
            auther=self.user
        )

    def test_home_page(self):
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home.html')

    def test_book_list_page(self):
        response = self.client.get(reverse('Book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BookList.html')
        self.assertContains(response, self.book.title)

    def test_book_details_page(self):
        response = self.client.get(reverse('Book_detals', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'BookDetails.html')
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book.description)
