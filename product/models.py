from django.db import models


# Create your models here.

class Product(models.Model):  # name of table
    title = models.CharField(max_length=300)
    price = models.IntegerField()
