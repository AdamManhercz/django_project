from django.test import TestCase, Client
from django.urls import reverse, resolve
from ..views import home, recipes, add_recipe


class TestUrls(TestCase):
    """Urls tests"""

    def setUp(self) -> None:

        self.client = Client()
        self.home_url = reverse("home")
        self.recipes_url = reverse("recipes")
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
        self.assertEqual(response.status_code, 302)

    def test_add_recipe_url(self):
        """Tests add_recipe url"""

        response = self.client.get(self.add_recipe_url)

        self.assertEqual(resolve(self.add_recipe_url).func, add_recipe)
        self.assertEqual(response.status_code, 200)
