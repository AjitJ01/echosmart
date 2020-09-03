from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    mo_numer = models.CharField(max_length=200)
