from django.core.management.base import BaseCommand
from food_planner.models import RecipeList
from ..data_scrape.recipe_scrape import Scraper 


class Command(BaseCommand):
    help = "Insert data into database "

    def handle(self, *args, **options):
        """Adds the collected data to the db"""

        scraper = Scraper()

        recipes, urls, images = scraper.get_recipe_info()

        for recipe, url, image in zip(recipes, urls, images):
            models = RecipeList(recipes=recipe, urls=url, images=image)
            models.save()