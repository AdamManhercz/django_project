"""Views"""

from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from .models import RecipeList
from .forms import ContactForm, AddRecipeForm
from .management.commands.upload_data import add_recipes_to_model

# Create your views here.

def home(request):
    """Home page"""

    return render(request, "food/home.html")

def recipes(request):
    """Shows the available recipes of the page"""

    add_recipes_to_model()

    random_recipes = RecipeList.objects.order_by("?")[:5]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    meal_items = zip(random_recipes, weekdays)

    random_recipes = RecipeList.objects.order_by("?")

    
    if request.method == "POST":
        name = request.user.username
        user_email = request.user.email
        message = render_to_string("email/email_template.html", {"name": name, "meal_items": meal_items})
        email = EmailMessage("Meal plan",
                                message, 
                                settings.EMAIL_HOST_USER, 
                                [user_email])
        try:
            email.send()
            return redirect("home")
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        
    context = {"random_recipes": random_recipes}
    return render(request,"food/recipes.html",context)

def contact(request): 
    """Creates the content and the sending mechanismi of the requested meal plan"""

    random_recipes = RecipeList.objects.order_by("?")[:5]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    meal_items = zip(random_recipes, weekdays)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['user_email']
            message = render_to_string("email/email_template.html", {"name": name, "meal_items": meal_items})
            email = EmailMessage("Meal plan",
                                  message, 
                                  settings.EMAIL_HOST_USER, 
                                  [user_email])
            try:
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect ("home")
    
    form = ContactForm()
    context = {'form': form}
    return render(request, "food/contact.html", context)

def add_recipe(request):
    """Creates the form to add new recipe to the database"""

    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = AddRecipeForm()

    form = AddRecipeForm()
    context = {'form': form}
    return render(request, 'food/add_recipe.html', context)
