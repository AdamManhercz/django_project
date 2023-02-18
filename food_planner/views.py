from django.shortcuts import render, redirect, HttpResponse
from .models import RecipeList
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def home(request):
    return render(request, "food/home.html",)


def food_planner(request):

    random_recipes = RecipeList.objects.order_by("?")[:5]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    item_list = zip(random_recipes, weekdays)

    return render(
        request,
        ("food/food_planner.html"),
        {"item_list":item_list},
    )

#def contact(request):
#	if request.method == 'POST':
#		form = ContactForm(request.POST)
#		if form.is_valid():
#			subject = "Meal plan" 
#			body = {
#			'name': form.cleaned_data['name'], 
#			'email': form.cleaned_data['email_address'], 
#			}
##message -> random_recipes
#			try:
#				send_mail(subject, message="", 'admin@example.com', ['admin@example.com']) 
#			except BadHeaderError:
#				return HttpResponse('Invalid header found.')
#			return redirect ("")
#      
#	form = ContactForm()
#	return render(request, "food/contact.html", {'form':form})
#
#