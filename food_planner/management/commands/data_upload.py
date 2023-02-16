import pandas as pd
from django.core.management.base import BaseCommand
from food_planner.models import RecipeList


class Command(BaseCommand):
    help = "Import recipes"

    def handle(self, *args, **options):
        """Add recipes to models"""

        df = pd.read_csv("recipe.csv")

        for recipe, url_link in zip(df.recipes, df.urls):
            models = RecipeList(recipes=recipe, url_links=url_link)
            models.save()
