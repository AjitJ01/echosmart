from django.db import models
from member_profile.models import *

class CustomerType(models.Model):
    class Meta:
        db_table = "customer_type"
    ctype = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')

class Customer(models.Model):
    class Meta:
        db_table = "customer"
    ctype = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    title = models.CharField(max_length=5, blank=False, default='')
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=200, blank=False, default='')
    pin = models.CharField(max_length=6, blank=False, default='')
    email = models.CharField(max_length=200, blank=False, default='')
    contact_no = models.CharField(max_length=12, blank=False, default='')
    alt_contact_no = models.CharField(max_length=12, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
    date_of_bith = models.DateField()
    proof_id = models.ForeignKey(IdProof, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/customer/id_proofs', blank=True)
