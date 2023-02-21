"""URL patterns in food_planner app"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipes, name="recipes"),
    path("contact/", views.contact, name="contact"),
    path("add_recipe/", views.add_recipe, name="add_recipe")
]
