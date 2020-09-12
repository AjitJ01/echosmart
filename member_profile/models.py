# from django.db import models

# class UserType(models.Model):
#     class Meta:
#         db_table = "user_type"
#     utype = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200, blank=False, default='')

# class CustomerType(models.Model):
#     class Meta:
#         db_table = "customer_type"
#     ctype = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200, blank=False, default='')

# class UserType(models.Model):
#     class Meta:
#         db_table = "user_type"
#     utype = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200, blank=False, default='')

# class UserType(models.Model):
#     class Meta:
#         db_table = "user_type"
#     utype = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200, blank=False, default='')
    
# class Product(models.Model):
#     class Meta:
#         db_table = "product"
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=70, blank=False, default='')
#     brand = models.CharField(max_length=70, blank=False, default='')
#     description = models.CharField(max_length=200, blank=False, default='')
#     price = models.IntegerField()
#     unit_of_measure = models.CharField(max_length=70, blank=False, default='')
#     image = models.ImageField(blank=True)


# class Inventory(models.Model):
#     class Meta:
#         db_table = "inventory"
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
