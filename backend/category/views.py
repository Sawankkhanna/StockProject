from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Category

resultData = []

@api_view(['GET'])
def getAllCategories(request):
    categories = Category.objects.all().values()

    categories_list = list(categories)

    return JsonResponse(categories_list, safe=False)