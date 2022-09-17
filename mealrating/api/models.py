from enum import unique
from operator import index
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db import models
from django.contrib.auth.models import User
class Meal(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    def __str__(self):
        return str(self.title)
class Rating(models.Model):
    meal=models.ForeignKey(Meal,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.meal)
    class Meta():
        unique_together=(('user','meal'),)#نفس اليوزر ما بنفع يعمل تقييم لنفس الوجبة
        index_together=(('user','meal'),)