from django.test import TestCase
from django.urls import reverse

from ..forms import AddRecipeForm

class TestForms(TestCase):
    """Forms tests"""

    def test_valid_addition(self):
        """Tests recipe addition with valid data"""

        recipe = {
            "recipes": "test recipe", 
            "urls":"https://www.example.com/testrecipe", 
            "images":"https://www.example.com/images/testrecipes.jpg"
            }
        form = AddRecipeForm(data=recipe)

        self.assertTrue(form.is_valid())

    def test_invalid_addition(self):
        """Tests recipe addition with invalid data"""

        recipe = {
            "recipes": "", 
            "urls":"https://www.example.com/testrecipe", 
            "images":"https://www.example.com/images/testrecipes.jpg"
            }
        form = AddRecipeForm(data=recipe)

        self.assertFalse(form.is_valid())

