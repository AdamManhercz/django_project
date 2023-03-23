from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework.parsers import JSONParser
from .models import RecipeList
from .serializers import RecipeListSerializer



class APIRecipesList(APIView):
    """List all recipes or create a new one"""

    def get(self, request, format=None):
        recipes = RecipeList.objects.all()
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = RecipeListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(f"The recipe was added successfully!")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Either the recipe is already in existence or the requested data does not follow the proper format.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class APIRecipeDetail(APIView):
    """Retrieve, update or delete a certain recipe."""

    def get_object(self, recipes):
        try:
            return RecipeList.objects.get(pk=recipes)
        except RecipeList.DoesNotExist:
            raise Http404
        
    def get(self, request, recipes, format=None):
        recipe = self.get_object(recipes)
        serializer = RecipeListSerializer(recipe)
        return Response(serializer.data)
    
    def delete(self, request, recipes, format=None):
        recipe = self.get_object(recipes)
        recipe.delete()
        print(f"The recipe was deleted successfully!")
        return Response(status=status.HTTP_204_NO_CONTENT)