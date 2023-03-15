"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from food_planner import views, rest_views
from users import views as user_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("register/", user_views.register, name="user_register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="user_logout"),
    path("recipes/", views.recipes, name="recipes"),
    path("contact/", views.contact, name="contact"),
    path("add_recipe/", views.add_recipe, name="add_recipe"),
    path("api/recipe_list", rest_views.APIRecipesList.as_view(), name="api_list"),
]








