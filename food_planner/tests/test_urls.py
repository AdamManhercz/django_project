from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import home, recipes, contact, add_recipe


class TestUrls(SimpleTestCase):
    """Urls tests"""

    def setUp(self) -> None:
        
        self.home_url = reverse("home")
        self.recipes_url = reverse("recipes")
        self.contact_url = reverse("contact")
        self.add_recipe_url = reverse("add_recipe")

    def test_home_url(self):
        """Tests home url"""

        self.assertEqual(resolve(self.home_url).func, home)

    def test_recipes_url(self):
        """Tests recipes url"""

        print(resolve(self.recipes_url))
        self.assertEqual(resolve(self.recipes_url).func, recipes)

    def test_contact_url(self):
        """Tests contact url"""

        print(resolve(self.contact_url))
        self.assertEqual(resolve(self.contact_url).func, contact)

    def test_add_recipe_url(self):
        """Tests add_recipe url"""

        print(resolve(self.add_recipe_url))
        self.assertEqual(resolve(self.add_recipe_url).func, add_recipe)