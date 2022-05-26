from django.db import models


# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    nacimiento = models.DateField()
    documento = models.IntegerField()
