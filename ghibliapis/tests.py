import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .test_data import FILM

class GetFilmTestCase(APITestCase):
    @classmethod
    def setUp(self):
        # SetUp required environment for tests
        # none needed in this case
        self.client = APIClient()
        self.film_url = reverse('film') + '?id=2baf70d1-42bb-4437-b551-e5fed5a87abe&API-KEY=apikey'
 
    def test_get_film(self):
        response = self.client.get(self.film_url)
        resp = json.loads(response.content)
        self.assertEqual(response.status_code,200)
        self.assertEqual(resp,FILM)
    
    def tearDown(self):
        # Clean up after each test
        pass