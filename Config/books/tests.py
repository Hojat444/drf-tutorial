from django.test import TestCase
from .models import Book

# Create your tests here.


class BookModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title = "my title",author = "my author",code = "1234")
        
    def test_title_content(self):
        book = Book.objects.get(id=1)
        title = f'{book.title}'
        self.assertEqual(title,"my title")
        
        
    def test_author_content(self):
        book = Book.objects.get(id=1)
        author = f'{book.author}'
        self.assertEqual(author,"my author")            