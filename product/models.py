from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "category"
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    image = models.ImageField(upload_to='images/category', blank=True)
    

class Product(models.Model):
    class Meta:
        db_table = "product"
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, blank=False, default='')
    brand = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    price = models.IntegerField()
    unit_of_measure = models.CharField(max_length=70, blank=False, default='')
    image = models.ImageField(blank=True)


class Inventory(models.Model):
    class Meta:
        db_table = "inventory"
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()