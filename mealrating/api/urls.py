from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register('meal',views.Mealviewset)
router.register('rating',views.Ratingviewset)
router.register('user',views.Userviewset)
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('api_authtoken',obtain_auth_token)
]