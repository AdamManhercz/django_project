from django.shortcuts import render
from .models import RecipeList

# Create your views here.


def food_planner(request):

    random_recipes = RecipeList.objects.order_by("?")[:5]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    item_list = zip(random_recipes, weekdays)

    return render(
        request,
        "food_planner/food_planner.html",
        {"item_list":item_list},
    )

def home(request):
    return render(request, "food_planner/home.html",)

