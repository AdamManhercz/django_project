from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from ..views import home, recipes, contact, add_recipe


class TestUrls(SimpleTestCase):
    """Urls tests"""

    def setUp(self) -> None:

        self.client = Client()
        self.home_url = reverse("home")
        self.recipes_url = reverse("recipes")
        self.contact_url = reverse("contact")
        self.add_recipe_url = reverse("add_recipe")

    def test_home_url(self):
        """Tests home url"""

        response = self.client.get(self.home_url)

        self.assertEqual(resolve(self.home_url).func, home)
        self.assertEqual(response.status_code, 200)

    def test_recipes_url(self):
        """Tests recipes url"""

        response = self.client.get(self.recipes_url)

        self.assertEqual(resolve(self.recipes_url).func, recipes)
        self.assertEqual(response.status_code, 200)


    def test_contact_url(self):
        """Tests contact url"""

        response = self.client.get(self.contact_url)

        self.assertEqual(resolve(self.contact_url).func, contact)
        self.assertEqual(response.status_code, 200)


    def test_add_recipe_url(self):
        """Tests add_recipe url"""

        response = self.client.get(self.add_recipe_url)

        self.assertEqual(resolve(self.add_recipe_url).func, add_recipe)
        self.assertEqual(response.status_code, 200)