from django.db import models
from member_profile.models import *

class UserType(models.Model):
    class Meta:
        db_table = "user_type"
    utype = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')

class User(models.Model):
    class Meta:
        db_table = "user"
        
    utype = models.ForeignKey(UserType, on_delete=models.CASCADE,null=True,blank = True)
    title = models.CharField(max_length=5, blank=False, default='')
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=200, blank=False, default='')
    pin = models.CharField(max_length=6, blank=False, default='')
    email = models.CharField(max_length=200, blank=False, default='')
    contact_no = models.CharField(max_length=12, blank=False, default='')
    alt_contact_no = models.CharField(max_length=12, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
    date_of_bith = models.DateField(null=True,blank = True)
    proof_id = models.ForeignKey(IdProof, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/user/id_proofs', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified_on = models.DateTimeField(auto_now=True)
    
class ActivityHistory(models.Model):
    class Meta:
        db_table = "activity_history"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operation = models.CharField(max_length=50, blank=False, default='')
    entity = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    time = models.TimeField()