from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from ..models import RecipeList
from ..forms import ContactForm, AddRecipeForm
from ..views import home



class TestViews(TestCase):
    """Views tests"""

    def setUp(self) -> None:
        
        self.client = Client()
        self.home_url = reverse("home")
        self.contact_url = reverse("contact")
        self.add_recipe_url = reverse("add_recipe")
    
    def test_home_view(self):
        """Tests the 'home' view"""
        
        response = self.client.get(self.home_url)

        # Check that the response uses the correct template
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "food/home.html")
    
## CONTACT VIEW TESTS

    def test_valid_form_submission_sends_email(self):
        """Tests email sending process"""

        form_data = {"name": "John", "user_email": "john@example.com"}
        response = self.client.post(self.contact_url, data= form_data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Meal plan")
        self.assertEqual(mail.outbox[0].to, "john@example.com")
        self.assertEqual(mail.outbox[0].from_email, "foodplanner.django@gmail.com")
     

    def test_invalid_form_submission_does_not_send_email(self):
        """Tests invalid email sending"""

        form_data = {"name": "John"}
        response = self.client.post(self.contact_url, form_data)
        self.assertEqual(len(mail.outbox), 0)


## ADD_RECIPE VIEW TESTS

    def test_valid_add_recipe(self):
        """Tests valid recipe addition"""

        form_data = {"recipes":"Recipe1", "urls":"http://recipe1.com", "images":"http://recipe1.com/image1.jpg"}

        response = self.client.post(self.add_recipe_url, form_data)

        self.assertEqual(response.status_code, 302) #should redirect to home page
        self.assertEqual(RecipeList.objects.count(), 1)

        new_recipe = RecipeList.objects.first()
        self.assertEqual(new_recipe.recipes, "Recipe1")


    def test_invalid_add_recipe(self):
        """Tests valid recipe addition"""

        form_data = {"recipes":"", "urls":"http://recipe1.com", "images":"http://recipe1.com/image1.jpg"}

        response = self.client.post(self.add_recipe_url, form_data)

        self.assertEqual(response.status_code, 200) #should render form again
        self.assertEqual(RecipeList.objects.count(), 0)

    def test_not_unique_add_recipe(self):
        """Tests valid recipe addition"""

        RecipeList.objects.create(recipes="Recipe1", urls="http://recipe1.com", images="http://recipe1.com/image1.jpg")

        form_data = {"recipes":"Recipe1", "urls":"http://recipe1.com", "images":"http://recipe1.com/image1.jpg"}

        response = self.client.post(self.add_recipe_url, form_data)

        self.assertEqual(response.status_code, 200) #should render form again
        self.assertEqual(RecipeList.objects.count(), 0)


    