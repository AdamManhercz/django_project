"""Views"""

from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect
from .models import RecipeList
from .forms import AddRecipeForm

# Create your views here.

def home(request):
    """Home page"""

    return render(request, "food/home.html")

def recipes(request):
    """Shows the available recipes of the page"""

    if not request.user.is_authenticated:
        return redirect("user_login")

    weekday_recipes = RecipeList.objects.order_by("?")[:5]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    meal_items = zip(weekday_recipes, weekdays)

    random_recipes = RecipeList.objects.order_by("?")

    if request.method == "POST":
        message = render_to_string(
            "email/email_template.html", 
            {"name": request.user.username, "meal_items": meal_items})
        email = EmailMessage("Meal plan",
                                message, 
                                settings.EMAIL_HOST_USER, 
                                [request.user.email])
        
        email.send()
        return redirect("home")
        
    context = {"random_recipes": random_recipes}
    return render(request,"food/recipes.html",context)

def add_recipe(request):
    """Creates the form to add new recipe to the database"""

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        
        if form.is_valid():
            recipe = form.cleaned_data['recipes']
            url = form.cleaned_data['urls']
            image = form.cleaned_data['images']
            
            if RecipeList.objects.filter(recipes=recipe).exists() or RecipeList.objects.filter(urls=url).exists() or RecipeList.objects.filter(images=image).exists():
                messages.error(request, 'This recipe already exists in the database')
                return redirect('add_recipe')
            
            form.save()
            messages.success(request, 'Recipe added successfully')
            return redirect('home')
    else:
        form = AddRecipeForm()

    context = {'form': form}
    return render(request, 'food/add_recipe.html', context)
