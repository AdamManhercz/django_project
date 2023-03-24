from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestUserViews(TestCase):
    """Test users views"""

    def setUp(self) -> None:
        
        self.registration_url = reverse("user_register")
        self.login_url = reverse("user_login")
        self.client = Client()

        self.valid_data = {
            "username": "test_user",
            "email": "test_user@test.com",
            "password1": "Userpass0101",
            "password2": "Userpass0101"
        }

        self.invalid_data = {
            "username": "test_user",
            "email": "test_usercom",
            "password1": "Userpass0101",
            "password2": "Userpass0101"
        }

    def test_valid_registration(self):

        response = self.client.post(self.registration_url, self.valid_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertEqual(User.objects.count(), 1)
    
    def test_invalid_registration(self):

        response = self.client.post(self.registration_url, self.invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

        


