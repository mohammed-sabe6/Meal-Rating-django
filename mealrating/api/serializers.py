from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from rest_framework.authtoken.views import Token


class Ratingserializer(serializers.ModelSerializer):
    class Meta():
        model=Rating
        fields='__all__'

class Mealserializer(serializers.ModelSerializer):
    class Meta():
        model=Meal
        fields=['title','description','number_of_rating','average_of_rating',]

class Userserializer(serializers.ModelSerializer):
    class Meta():
        model=User
        fields=['id','username','password']
        extra_kwargs={'password':{'write_only':True,'required':True}}
    # def create(self,validated_data):
    #     user=User.objects.create_user(**validated_data)
    #     token=Token.objects.create(user=user)
    #     return token