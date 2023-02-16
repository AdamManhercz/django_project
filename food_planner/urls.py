"""URL patterns in food_planner app"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("food_planner/", views.food_planner, name="food_planner"),
]
