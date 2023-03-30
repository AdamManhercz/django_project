from django.urls import reverse
from django.conf import settings
from ..models import RecipeList
from ..rest_views import APIRecipeDetail
from rest_framework import status
from django.http import Http404
from rest_framework.test import APITestCase, APIClient
from ..serializers import RecipeListSerializer



class TestViews(APITestCase):
    """API views tests"""

    def setUp(self) -> None:
         
        self.api_client = APIClient()
        self.api_url = reverse("api_list")
        
        RecipeList.objects.create(
            recipes='Spaghetti Carbonara',
            urls="https://www.example.com/recipe/carbonara",
            images="https://www.example.com/images/carbonara.jpg",
        )

        self.test_data = {
            "recipes": "test recipe", 
            "urls":"https://www.example.com/testrecipe", 
            "images":"https://www.example.com/images/testrecipes.jpg"
            }
         
    def test_api_recipes(self):
        """Tests API GET"""

        response = self.api_client.get(self.api_url)
        recipes = RecipeList.objects.all()
        serializer = RecipeListSerializer(recipes, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_object_fail(self):
        view = APIRecipeDetail()
        with self.assertRaises(Http404):
            view.get_object("Rántott hús")  # Invalid recipe ID

    def test_api_post_recipe(self):
        """Tests API POST"""

        response = self.api_client.post(self.api_url, self.test_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_non_unique_post(self):
        """Tests API POST for non_unique data"""
         
        non_unique_post_data = {
            "recipes":'Spaghetti Carbonara',
            "urls":"https://www.example.com/recipe/carbonara",
            "images":"https://www.example.com/images/carbonara.jpg",
        }
         
        response = self.api_client.post(self.api_url, non_unique_post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_invalid_post(self):
        """Tests API POST for invalid data"""
         
        non_unique_post_data = {
            "recipes":'',
            "urls":"https://www.example.com/recipe/carbonara",
            "images":"https://www.example.com/images/carbonara.jpg",
        }
         
        response = self.api_client.post(self.api_url, non_unique_post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_recipe(self):
        """Tests GET single recipe"""

        self.api_client.post(self.api_url, self.test_data, format='json')
        response = self.api_client.get(f'{self.api_url}/{self.test_data["recipes"]}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_delete_recipe(self):
        """Tests API DELETE"""

        self.api_client.post(self.api_url, self.test_data, format='json')
        response = self.api_client.delete(f'{self.api_url}/{self.test_data["recipes"]}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

       


    



        


    