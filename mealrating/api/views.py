import json
from logging import raiseExceptions
from urllib import response
from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authtoken.views import Token
class Userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()

    serializer_class=Userserializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializers=self.get_serializer(data=request.data)#بدي اخذ داتا من الريكوست
        serializers.is_valid(raise_exception=True)
        self.perform_create(serializers)#تعمل بيرفورم جديد  للسيرلزر
        token,created=Token.objects.get_or_create(user=serializers.instance)#تنشأ توكن ثم تعرضه لك كمستخدم
        return Response({'token':token.key},status=status.HTTP_201_CREATED)
    def list(self, request, *args, **kwargs):
        response={
            'message':'you cant list user'
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        response={
            'message':'you cant delete user'
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST) 
    def put(self,request,pk):
        user=get_object_or_404(User,pk=pk)
        serializers=Userserializer(user,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class Mealviewset(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=Mealserializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated]
    @action(methods=["post"],detail=True)
    def meal_pk(self,request,pk=None):
        if 'stars' in request.data:
            # username=request.data['username']
            # user=User.objects.get(username=username)
            user=request.user
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
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated]#التيست يكون من header
    def create(self, request, *args, **kwargs):
        json={
            'message':'invalid way to create'
        }
        return Response(json,status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, *args, **kwargs):
        json={
            'message':'invalid way to update'
        }
        return Response(json,status=status.HTTP_400_BAD_REQUEST)
    