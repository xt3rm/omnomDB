from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model):

    def __str__(self):
        return self.name.encode('UTF-8')

       

    name = models.CharField(max_length=500)
    kcal = models.DecimalField(max_digits=10, decimal_places=3)
    protein = models.DecimalField(max_digits=10, decimal_places=3)
    fat = models.DecimalField(max_digits=10, decimal_places=3)
    carb  = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.CharField(max_length=10)

class UserGoal(models.Model):

    def __str__(self):
        return  User.objects.get(username=self.userID).username.encode('UTF-8')

    userID  = models.ForeignKey(User,)
    kcal = models.DecimalField(max_digits=10, decimal_places=3)
    protein = models.DecimalField(max_digits=10, decimal_places=3)
    fat = models.DecimalField(max_digits=10, decimal_places=3)
    carb  = models.DecimalField(max_digits=10, decimal_places=3)

class JournalEntry(models.Model):

    userID = models.ForeignKey(User,)
    foodID = models.ForeignKey(Food,)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    tm = models.DateTimeField(auto_now=False,auto_now_add=True)


