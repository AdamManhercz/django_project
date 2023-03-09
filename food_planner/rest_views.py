from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RecipeList
from .serializers import RecipeListSerializer
from  rest_framework.parsers import JSONParser


@csrf_exempt
def recipes_list(request):
    """List all recipes or create a new one"""

    if request.method == 'GET':
        snippets = RecipeList.objects.all()
        serializer = RecipeListSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecipeListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)