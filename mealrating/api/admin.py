from django.contrib import admin
from .models import *
class RatingAdmin(admin.ModelAdmin):
    list_display=['id','user','meal','stars']
    list_filter=['user','meal']
    
class MealAdmin(admin.ModelAdmin):
    list_display=['id','title','description']
    list_filter=['title',]
    search_fields=['title','description',]
admin.site.register(Rating,RatingAdmin)
admin.site.register(Meal,MealAdmin)