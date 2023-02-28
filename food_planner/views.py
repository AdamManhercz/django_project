from django.shortcuts import render, redirect, HttpResponse
from .models import RecipeList
from .forms import ContactForm, AddRecipeForm
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, "food/home.html")

def recipes(request):

    random_recipes = RecipeList.objects.order_by("?")
    context = {"random_recipes": random_recipes}

    return render(request,"food/recipes.html",context)

def contact(request): 
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
        return redirect ("recipes/")
    
    form = ContactForm()
    context = {'form': form}
    return render(request, "food/contact.html", context)


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        
        if form.is_valid():
            form.save()
        else:
            form = AddRecipeForm()

    form = AddRecipeForm()
    context = {'form': form}
    return render(request, 'food/add_recipe.html', context)

