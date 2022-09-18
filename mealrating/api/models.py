
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db import models
from django.contrib.auth.models import User
class Meal(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
 
    def number_of_rating(self):
        rating=Rating.objects.filter(meal=self)
        return len(rating)
    def average_of_rating(self):
        sum=0
        rating=Rating.objects.filter(meal=self)
        for x in rating:
            sum += x.stars 
            if len(rating)>0:
                return sum/len(rating)
            else:
                return 0
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