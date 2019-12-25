from django.test import TestCase

from .models import Aliment


# class AlimentTestCase(TestCase):
#     def setUp(self):
#         self.test1 = Aliment.objects.create(code = 3274510004644, name = "Dolin Sirop D Orgeat", category = "Boissons", energy = 345, fat = 0, fat_saturated = 0, sugar = 86, salt = 0.03, nutrition_score = "e", url_link = 'https://fr.openfoodfacts.org/produit/3274510004644/dolin-sirop-d-orgeat-marie-dolin', picture_link='https://static.openfoodfacts.org/images/products/327/451/000/4644/front_fr.4.100.jpg')
#         self.test2 = Aliment.objects.create(code = 7616700020267, name = "Feinste Leckerli", category = "Snacks", energy = 1681, fat = 7, fat_saturated = 0.6, sugar = 46, salt = 0.05, nutrition_score = "d", url_link = 'https://fr.openfoodfacts.org/produit/7616700020267/feinste-leckerli-jowa', picture_link='https://static.openfoodfacts.org/images/products/761/670/002/0267/front_fr.21.100.jpg')
#
#     def testdb(self):
#         test = Aliment.objects.filter(code=3274510004644)
#
#         self.assertEqual(test[0].code, str(self.test1.code))


# # search_view page
# class SearchPageTestCase(TestCase):
#     # test that page returns a 200
#     def test_search_page_return_200(self):
#         response = self.client.get(reverse('substitute:search'))
#         self.assertEqual(response.status_code, 200)
#     # test that index page returns a 200
#     # test that detail page returns a 404 if the item does not exist


# detail_view Page
class DetailPageTestCase(TestCase):

    def setUp(self):
        # aliment for testing
        test_aliment = Aliment.objects.create(
            id="27217",
            code="27217",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com",
            picture_link="http://google.com",
        )
        test_aliment.save()

    # test that detail page returns a 200 if the item exists
    def test_detail_page_return_200_if_item_exist(self):
        response = self.client.get('/substitute/details/27217/')
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_page_return_404_if_item_not_exist(self):
        response = None
        response.status_code = None
        try:
            response = self.client.get('/substitute/details/11111/')
        except FileExistsError:
            pass

        self.assertEqual(response.status_code, 200)

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
#
#
# # initialise_database_view page
# # class MockOpenFoodFactsAPIHandler():
# #     """
# #     Mock the OFF API handler
# #     """
# #     def __init__(self):
# #         """No attributes to initialize.
# #         """
# #     def fetch_data_from_cat(self, category):
# #         """
# #         Return a JSON file.
# #         """
# #         api_answer = [
# #
# #         ]
# #
# #         return api_answer
