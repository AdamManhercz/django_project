from django.core.management.base import BaseCommand
from food_planner.models import RecipeList
from ..data_scrape.recipe_scrape import Scraper 
from ..data_scrape.recipe_api import EdamamApi 


class Command(BaseCommand):
    help = "Add recipes to RecipeList"

    def handle(self, *args, **options):

        e = EdamamApi()
        scraper = Scraper()

        api_recipes, api_urls, api_images = e.get_recipe_api()
        scrape_recipes, scrape_urls, scrape_images = scraper.get_recipe_info()

        recipes = api_recipes + scrape_recipes
        urls = api_urls + scrape_urls
        images = api_images + scrape_images

        for recipe, url, image in zip(recipes, urls, images):
            models = RecipeList(recipes=recipe, urls=url, images=image)
            models.save()
