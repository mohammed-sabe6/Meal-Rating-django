
from rest_framework import serializers
from .models import *
class Ratingserializer(serializers.ModelSerializer):
    class Meta():
        model=Rating
        fields='__all__'

class Mealserializer(serializers.ModelSerializer):
    class Meta():
        model=Meal
        fields=['title','description','number_of_rating','average_of_rating',]
