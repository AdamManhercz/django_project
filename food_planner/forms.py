from django import forms
from .models import RecipeList

class ContactForm(forms.Form):

    name = forms.CharField(max_length=100)
    user_email = forms.EmailField(max_length=100)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeList
        fields = ["recipes", "urls", "images"]
        labels = {'recipes': "Name of the food", "urls": "Url of the recipe", "images": "Source of its image"}
    