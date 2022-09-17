from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
class Mealviewset(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=Mealserializer

class Ratingviewset(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=Ratingserializer