from django.http import request
from django.test import TestCase
from django.urls import reverse

from accounts.models import MyUser
from .models import Aliment, UserLinkToAlimentsTable


# search_view page
class SearchPageTestCase(TestCase):

    def setUp(self):
        """ Load some aliment in the DB.
        """

        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

        aliment_2 = Aliment.objects.create(
            id="02",
            code="2",
            name="Oignons",
            category="legumes",
            energy="2",
            fat="2",
            fat_saturated="2",
            sugar="2",
            salt="2",
            nutrition_score="b",
            url_link="http://google.com/2",
            picture_link="http://google.com/2",
        )
        aliment_2.save()

    # test that page returns a 200
    def test_search_page_without_search_word(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': ''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Vous n'avez pas spécifié votre recherche. Voici notre liste."
                         )

    def test_search_page_with_a_known_search_word(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': 'patate'})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(str(response.context['message']),
                            "Vous n'avez pas spécifié votre recherche. Voici notre liste."
                            )
        self.assertEqual(response.context['substitutes'].object_list[1].name,
                         "Oignons"
                         )
        self.assertNotEqual(response.context['substitutes'].object_list[1].name,
                            "Patate"
                            )

    def test_search_page_with_a_unknown_search_word(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': 'chocolat'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Misère de misère, nous n'avons trouvé aucun résultat !"
                         )


# detail_view Page
class DetailPageTestCase(TestCase):

    def setUp(self):
        """ Load some aliment in the DB.
        """

        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

    # test that detail page returns a 200
    def test_detail_page_with_a_known_item(self):
        response = self.client.get('/substitute/details/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['aliment'].category), 'legumes')


# favorites_view page
class FavoritePageTestCase(TestCase):

    def setUp(self):
        """ Load some aliment in the DB.
        """

        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

        aliment_2 = Aliment.objects.create(
            id="02",
            code="2",
            name="Oignons",
            category="legumes",
            energy="2",
            fat="2",
            fat_saturated="2",
            sugar="2",
            salt="2",
            nutrition_score="b",
            url_link="http://google.com/2",
            picture_link="http://google.com/2",
        )
        aliment_2.save()

        test_user_1 = MyUser.objects.create_user(email="Franco13@.com",
                                                 first_name="claude",
                                                 name="francois",
                                                 password="Chanson"
                                                 )
        test_user_1.save()
        # User is authenticated
        self.client.login(username="Franco13@.com", password="Chanson")

    # test that page returns a 200
    def test_favorite_page_with_favorites(self):
        # Create link between aliments and user
        link_1 = UserLinkToAlimentsTable.objects.create(
            user_id="Franco13@.com",
            aliment_id=0
        )
        link_1.save()

        link_2 = UserLinkToAlimentsTable.objects.create(
            user_id="Franco13@.com",
            aliment_id=1
        )
        link_2.save()

        response = self.client.get(reverse('substitute:favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Voici vos favoris"
                         )

    def test_favorite_page_without_favorites(self):
        response = self.client.get(reverse('substitute:favorites'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Misère de misère, vous n'avez encore pas enregistrer de favoris !"
                         )

# # save_view page
# class SavePageTestCase(TestCase):
#     aliment_1 = Aliment.objects.create(
#         id="01",
#         code="1",
#         name="Patate",
#         category="legumes",
#         energy="1",
#         fat="1",
#         fat_saturated="1",
#         sugar="1",
#         salt="1",
#         nutrition_score="a",
#         url_link="http://google.com/1",
#         picture_link="http://google.com/1",
#     )
#     aliment_1.save()
#
#     test_user_1 = MyUser.objects.create_user(email="Franco13@.com",
#                                              first_name="claude",
#                                              name="francois",
#                                              password="Chanson"
#                                              )
#     test_user_1.save()
#
#     # test that page returns a 200
#     def test_save_page_return_200(self):
#         # URL return
#
#         # Send a url
#         response = self.client.get(reverse('substitute:save', args=[1231]))
#         self.assertEqual(response.status_code, 200)
#     # test that index page returns a 200

#
#
# # save_view page
# class DeletePageTestCase(TestCase):
#     # test that page returns a 200
#     def test_delete_page_return_200(self):
#         response = self.client.get(reverse('substitute:delete'))
#         self.assertEqual(response.status_code, 200)
#     # test that index page returns a 200
#
#
# # favorites_view page
# class FavoritePageTestCase(TestCase):
#     # test that page returns a 200
#     def test_favorite_page_return_200(self):
#         response = self.client.get(reverse('substitute:favorites'))
#         self.assertEqual(response.status_code, 200)
#     # test that index page returns a 200
