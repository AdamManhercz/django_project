from django.test import TestCase, Client
from django.urls import reverse, resolve
from ..views import register

class TestUserUrls(TestCase):
    """Urls tests"""

    def setUp(self) -> None:

        self.client = Client()
        self.register_url = reverse("user_register")


    def test_registration_url(self):

        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(self.register_url).func, register)