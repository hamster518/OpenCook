from django.shortcuts import render
from .models import Recipe
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

def get_recipes_api(request):
	recipes = Recipe.objects.all()
	data = serializers.serialize("json", recipes)

	return JsonResponse({'data':data})