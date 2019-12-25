from django.test import TestCase
from django.urls import reverse

from accounts.models import MyUser


# my_account_view page
class AccountPageTestCase(TestCase):

    def setUp(self):
        """Create a user for testing.
        """
        test_user = MyUser.objects.create_user(email="Franco13@.com",
                                               first_name="claude",
                                               name="francois",
                                               password="Chanson"
                                               )
        test_user.save()

    # test that page returns 200
    def test_account_page_return_200_when_user_connected(self):
        # User is authenticated
        self.client.login(username="Franco13@.com", password="Chanson")
        response = self.client.get(reverse('accounts:myAccount'))

        self.assertEqual(str(response.context['user']), "Franco13@.com")
        self.assertEqual(response.status_code, 200)

    # test that page doesn't return 200
    def test_account_page_return_200_when_user_not_connected(self):
        # User is not authenticated
        response = self.client.get(reverse('accounts:myAccount'))

        self.assertNotEqual(response.status_code, 200)


# signup_view page
class SignupPageTestCase(TestCase):

    # test that page returns a 200
    def test_signup_page_return_200_without_a_POST_method(self):
        # Request contains doesn't contain a POST
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_return_200_with_a_POST_method(self):
        # Request contains doesn't contain a POST
        response = self.client.post(reverse('accounts:signup'), data={'email': 'hubert.f@gmail.com',
                                                                      'first_name': 'hubert',
                                                                      'name': 'f'})
        self.assertEqual(response.status_code, 200)


# login_view page
class LoginPageTestCase(TestCase):

    # test that page returns a 200
    def test_login_page_return_200_without_a_POST_method(self):
        # Request contains doesn't contain a POST
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_return_200_with_a_POST_method(self):
        # Request contains doesn't contain a POST
        response = self.client.post(reverse('accounts:signup'), data={'username': 'hubert.f@gmail.com',
                                                                      'password': 'hubert'})
        self.assertEqual(response.status_code, 200)


# logout_view page
class LogoutPageTestCase(TestCase):

    def setUp(self):
        """Create a user for testing.
        """
        test_user = MyUser.objects.create_user(email="Franco13@.com",
                                               first_name="claude",
                                               name="francois",
                                               password="Chanson"
                                               )
        test_user.save()

    # test that page returns a 200
    def test_logout_page_return_200_when_user_connected(self):
        # Connect an user
        self.client.login(username="Franco13@.com", password="Chanson")
        # Disconnect him
        response = self.client.get(reverse('accounts:logout'))
        self.assertNotEqual(str(response.context['user']), "Franco13@.com")
        self.assertEqual(response.status_code, 200)

# test that page returns a 200
    def test_logout_page_return_200_when_user_not_connected(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertNotEqual(response.status_code, 200)

