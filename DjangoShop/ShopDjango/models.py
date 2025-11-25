from django.db import models

# Create your models here.

class Cart(models.Model):
    Item = models.CharField(max_length=50)
    Final_Price = models.CharField(max_length=50)

class Item(models.Model):
    Name = models.CharField(max_length=150)
    Price = models.CharField(max_length=150)