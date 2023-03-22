from rest_framework import status
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)