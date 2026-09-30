from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterUserTest(TestCase):

    def test_register_page_loads(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    def test_user_can_register_with_valid_data(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'novousuario',
            'password1': 'senhaSuperForte123',
            'password2': 'senhaSuperForte123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='novousuario').exists())

    def test_register_fails_with_mismatched_passwords(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'outrousuario',
            'password1': 'senhaForte123',
            'password2': 'senhaDIFERENTE456',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='outrousuario').exists())
        self.assertContains(response, 'não correspondem')


class LoginLogoutTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='senha12345')

    def test_login_page_loads(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_with_correct_credentials(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'teste',
            'password': 'senha12345',
        })
        self.assertEqual(response.status_code, 302)

    def test_login_with_wrong_password_fails(self):
        response = self.client.post(reverse('accounts:login'), {
            'username': 'teste',
            'password': 'senhaerrada',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout_redirects_to_book_list(self):
        self.client.login(username='teste', password='senha12345')
        response = self.client.post(reverse('accounts:logout'))
        self.assertRedirects(response, reverse('books:book'))