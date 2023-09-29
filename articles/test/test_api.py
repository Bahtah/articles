from django.urls import reverse
from rest_framework.test import APITestCase


class ArticlesApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('category-list')
        response = self.client.get(url)
        return response.data

