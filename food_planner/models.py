from django.db import models


class RecipeList(models.Model):
    """Recipe list model"""

    recipes = models.CharField(max_length=250, primary_key=True ,unique=True)
    urls = models.URLField(max_length=200, unique=True)
    images = models.CharField(max_length=350, unique=True)

    def __str__(self):
        return f"{self.recipes}"
