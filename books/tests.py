from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import AuthorModels, BookModel


class BookModelTest(TestCase):

    def setUp(self):
        self.author = AuthorModels.objects.create(name='Machado de Assis')

    def test_book_str_representation(self):
        book = BookModel.objects.create(
            title='Dom Casmurro',
            author=self.author,
            publication_year=1899,
        )
        self.assertEqual(str(book), 'Machado de Assis - Dom Casmurro')

    def test_available_defaults_to_true(self):
        book = BookModel.objects.create(
            title='Dom Casmurro',
            author=self.author,
            publication_year=1899,
        )
        self.assertTrue(book.available)


class BookListViewTest(TestCase):

    def setUp(self):
        self.author = AuthorModels.objects.create(name='George Orwell')
        self.book = BookModel.objects.create(
            title='1984',
            author=self.author,
            publication_year=1949,
        )

    def test_list_view_status_code(self):
        response = self.client.get(reverse('books:book'))
        self.assertEqual(response.status_code, 200)

    def test_book_appears_in_list(self):
        response = self.client.get(reverse('books:book'))
        self.assertContains(response, '1984')

    def test_search_by_title(self):
        response = self.client.get(reverse('books:book'), {'search': '1984'})
        self.assertContains(response, '1984')

    def test_search_by_author_name(self):
        response = self.client.get(reverse('books:book'), {'search': 'Orwell'})
        self.assertContains(response, '1984')

    def test_search_with_no_match(self):
        response = self.client.get(reverse('books:book'), {'search': 'Livro Inexistente'})
        self.assertNotContains(response, '1984')


class BookCreateViewTest(TestCase):

    def setUp(self):
        self.author = AuthorModels.objects.create(name='J.K. Rowling')
        self.user = User.objects.create_user(username='teste', password='senha12345')

    def test_redirects_to_login_if_not_authenticated(self):
        response = self.client.get(reverse('books:register'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_authenticated_user_can_create_book(self):
        self.client.login(username='teste', password='senha12345')

        response = self.client.post(reverse('books:register'), {
            'title': 'Harry Potter',
            'author': self.author.id,
            'category': 'Fantasia',
            'publication_year': 1997,
            'isbn': '1111111111',
            'available': True,
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(BookModel.objects.filter(title='Harry Potter').exists())


class BookUpdateDeleteViewTest(TestCase):

    def setUp(self):
        self.author = AuthorModels.objects.create(name='Clarice Lispector')
        self.book = BookModel.objects.create(
            title='A Hora da Estrela',
            author=self.author,
            publication_year=1977,
        )
        self.user = User.objects.create_user(username='teste', password='senha12345')
        self.client.login(username='teste', password='senha12345')

    def test_update_book(self):
        response = self.client.post(
            reverse('books:edit', args=[self.book.id]),
            {
                'title': 'A Hora da Estrela - Edição Especial',
                'author': self.author.id,
                'category': 'Romance',
                'publication_year': 1977,
                'isbn': '2222222222',
                'available': True,
            }
        )
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'A Hora da Estrela - Edição Especial')

    def test_delete_book(self):
        response = self.client.post(reverse('books:delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(BookModel.objects.filter(id=self.book.id).exists())