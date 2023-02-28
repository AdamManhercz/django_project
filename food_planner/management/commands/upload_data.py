import pandas as pd
from django.core.management.base import BaseCommand
from food_planner.models import RecipeList
from data_scrape.recipe_scrape import Scraper


class Command(BaseCommand):
    help = "Add recipes to RecipeList"

    def handle(self, *args, **options):

        recipes, urls, images = Scraper.get_recipe_info()
        for recipe, url, image in zip(recipes, urls, images):
            models = RecipeList(recipes=recipe, urls=url, images=image)
            models.save()
