from django.test import TestCase
from django.urls import reverse
from .models import Aliment


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
    def test_search_page_return_200_without_search_word(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': ''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Vous n'avez pas spécifié votre recherche. Voici notre liste."
                         )

    def test_search_page_return_200_with_search_word(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': 'patate'})
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(str(response.context['message']),
                         "Vous n'avez pas spécifié votre recherche. Voici notre liste."
                         )
        self.assertEqual(response.context['substitutes'].object_list[1].name,
                         "Oignons"
                         )


    # test that index page returns a 200
    # test that detail page returns a 404 if the item does not exist


# # detail_view Page
# class DetailPageTestCase(TestCase):
#
#     def setUp(self):
#         # aliment for testing
#         test_aliment = Aliment.objects.create(
#             id="27217",
#             code="27217",
#             name="Patate",
#             category="legumes",
#             energy="1",
#             fat="1",
#             fat_saturated="1",
#             sugar="1",
#             salt="1",
#             nutrition_score="a",
#             url_link="http://google.com",
#             picture_link="http://google.com",
#         )
#         test_aliment.save()
#
#     # test that detail page returns a 200 if the item exists
#     def test_detail_page_return_200_if_item_exist(self):
#         response = self.client.get('/substitute/details/27217/')
#         self.assertEqual(response.status_code, 200)
#
#     # test that detail page returns a 404 if the item does not exist
#     def test_detail_page_return_404_if_item_not_exist(self):
#         response = None
#         response.status_code = None
#         try:
#             response = self.client.get('/substitute/details/11111/')
#         except FileExistsError:
#             pass
#
#         self.assertEqual(response.status_code, 200)

# # save_view page
# class SavePageTestCase(TestCase):
#
#     # def __init__(self):
#     #     # Aliment
#     #     self.aliment = {
#     #         "code": "123459",
#     #         "product_name": "Patato",
#     #         "categories": "legumes",
#     #         "energy_value": "100",
#     #         "fat_value": "101",
#     #         "saturated-fat_value": "102",
#     #         "sugars_value": "103",
#     #         "salt_value": "104",
#     #         "nutrition_grade_fr": "a",
#     #         "Open_food_facts_url": "openfoodfacts/patate.com",
#     #         "image_thumb_url": "openfoodfacts/patatepic.com",
#     #     }
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
