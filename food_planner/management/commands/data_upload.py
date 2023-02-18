import pandas as pd
from django.core.management.base import BaseCommand
from food_planner.models import RecipeList


class Command(BaseCommand):
    help = "Add recipes to RecipeList"

    def handle(self, *args, **options):

        df = pd.read_csv("recipes.csv", delimiter=",")

        for recipe, url, image in zip(df.recipes, df.urls, df.images):
            models = RecipeList(recipes=recipe, urls=url, images=image)
            models.save()
