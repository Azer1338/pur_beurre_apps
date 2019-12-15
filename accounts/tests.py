from django.test import TestCase
from django.urls import reverse


# my_account_view page
class AccountPageTestCase(TestCase):
    # test that page returns a 200
    def test_account_page_return_200(self):
        response = self.client.get(reverse('accounts:myAccount'))
        self.assertEqual(response.status_code, 200)

        #
    # def test_index_page(self):
    #     # response = self.client.get(reverse('myAccount'))
    #     # self.assertEqual(response.status_code, 200)
    #     self.assertEqual("a","a")


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


