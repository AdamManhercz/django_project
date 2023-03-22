from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from django.conf import settings
from ..models import RecipeList


class TestViews(TestCase):
    """Views tests"""

    def setUp(self) -> None:
        
        self.client = Client()
        self.auth_client = Client()
        self.home_url = reverse("home")
        self.add_recipe_url = reverse("add_recipe")
        self.recipes_url = reverse("recipes")

        RecipeList.objects.create(
            recipes='Spaghetti Carbonara',
            urls='https://www.example.com/recipe/carbonara',
            images='https://www.example.com/images/carbonara.jpg',
        )

        self.user = User.objects.create_user(
            username="testuser", 
            email="testuser@test.com", 
            password="testpass")

## HOME VIEW TEST
    def test_home_view(self):
        """Tests the 'home' view"""
        
        response = self.client.get(self.home_url)

        # Check that the response uses the correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "food/home.html")


## ADD_RECIPE VIEW TESTS
    def test_unique_recipe_addition(self):
        """Tests valid recipe addition"""

        unique_data = {"recipes":'Rántott hús', 
                    "urls":'https://www.example.com/recipe/rantotthus', 
                    "images":'https://www.example.com/images/rantotthus.jpg'
                    }

        response = self.client.post(self.add_recipe_url, unique_data)

        self.assertEqual(response.status_code, 302) #should redirect to home page
        self.assertEqual(RecipeList.objects.count(), 2)

        new_recipe = RecipeList.objects.first()
        self.assertEqual(new_recipe.recipes, "Rántott hús")

    def test_non_unique_recipe_addition(self):
        """Tests valid recipe addition"""

        non_unique_data = {"recipes":'Spaghetti Carbonara', 
                    "urls":'https://www.example.com/recipe/carbonara', 
                    "images":'https://www.example.com/images/carbonara.jpg'
                    }

        response = self.client.post(self.add_recipe_url, non_unique_data)

        self.assertEqual(response.status_code, 200) #should render form again
        self.assertEqual(RecipeList.objects.count(), 1)


## RECIPES VIEW TESTS

    def test_authenticated_user_can_access_view(self):
        """Authenticated user can access the view"""

        self.auth_client.login(username = self.user.username, password = self.user.password)
        response =self.auth_client.get(self.recipes_url)

        self.assertEqual(response.status_code, 302)

    def test_send_email(self):
        """Email sending succeed"""

        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.recipes_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Meal plan')
        self.assertEqual(mail.outbox[0].to, [self.user.email])
        self.assertEqual(mail.outbox[0].from_email, settings.EMAIL_HOST_USER)



        


    