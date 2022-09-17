from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
router.register('meal',views.Mealviewset)
router.register('rating',views.Ratingviewset)
urlpatterns = [
    path('api/viewset/',include(router.urls))
]