from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

class Mealviewset(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=Mealserializer
    @action(methods=["post"],detail=True)
    def meal_pk(self,request,pk=None):
        if 'stars' in request.data:
            username=request.data['username']
            user=User.objects.get(username=username)
            stars=request.data['stars']
            meal=Meal.objects.get(id=pk)
            try:
                rate=Rating.objects.get(user=user.id,meal=meal.id)
                rate.stars=stars
                rate.save()
                serializers=Ratingserializer(rate,many=False)
                json={
                    'message':'Meal Reating Update',
                    'result':serializers.data
                }
                return Response(json,status=status.HTTP_400_BAD_REQUEST)
            except:
                rate=Rating.objects.create(stars=stars,meal=meal,user=user)
                serializers=Ratingserializer(rate,many=False)
                json={
                    'message':'Meal Reating Create',
                    'result':serializers.data
                          }
                return Response(json,status=status.HTTP_200_OK)
        else:
            json={
                'message':'stars not provied'
            }
            return Response(json,status=status.status.HTTP_400_BAD_REQUEST)
class Ratingviewset(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=Ratingserializer