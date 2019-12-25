from importlib import import_module

from django.conf import settings
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import MyUser


# my_account_view page
class AccountPageTestCase(TestCase):

    def setUp(self):
        # Create a user for testing
        test_user = MyUser.objects.create_user(email="Franco13@.com", first_name="claude", name="francois", password="Chanson")
        test_user.save()

    # test that page returns a 200
    def test_account_page_return_200_when_user_connected(self):
        # User is authentified
        self.client.login(username="Franco13@.com", password="Chanson")
        response = self.client.get(reverse('accounts:myAccount'))

        self.assertEqual(str(response.context['user']), "Franco13@.com")
        self.assertEqual(response.status_code, 200)

    def test_account_page_return_200_when_user_not_connected(self):
        # User is authentified
        response = self.client.get(reverse('accounts:myAccount'))

        self.assertNotEqual(response.status_code, 200)


# signup_view page
class SignupPageTestCase(TestCase):
    # test that page returns a 200
    def test_signup_page_return_200(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
    # test that index page returns a 200
    # test the POST
    # test the user generation form
    # Test the user in the database


# login_view page
class LoginPageTestCase(TestCase):
    # test that page returns a 200
    def test_login_page_return_200(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
    # test that index page returns a 200
    # test the POST
    # test the authentification form
    # Test that the user is redirect to the previous page


# logout_view page
class LogoutPageTestCase(TestCase):
    # test that page returns a 200
    def test_login_page_return_200(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 200)
    # test that index page returns a 200
    # test that the user is deconnected


