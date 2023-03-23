from django.urls import reverse
from django.conf import settings
from ..models import RecipeList
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ..serializers import RecipeListSerializer



class TestViews(APITestCase):

    def setUp(self) -> None:
         
         self.api_client = APIClient()
         self.api_url = reverse("api_list")

         self.test_data = {
            "recipes": "test recipe", 
            "urls":"https://www.example.com/testrecipe", 
            "images":"https://www.example.com/images/testrecipes.jpg"
            }


## API VIEWS TESTS

    def test_api_recipes(self):
            """Tests API GET"""

            response = self.api_client.get(self.api_url)
            recipes = RecipeList.objects.all()
            serializer = RecipeListSerializer(recipes, many=True)

            self.assertEqual(response.data, serializer.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_post_recipe(self):
        """Tests API POST"""

        response = self.api_client.post(self.api_url, self.test_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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

       


    



        


    