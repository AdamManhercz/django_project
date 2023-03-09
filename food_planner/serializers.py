from rest_framework import serializers
from .models import RecipeList


class RecipeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeList
        fields = ["recipes", "urls", "images"]