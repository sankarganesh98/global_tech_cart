from django.db import models
from django.contrib.auth.models import User
from enterprise.models import Enterprise
# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    enterprise = models.ForeignKey(Enterprise, models.DO_NOTHING)
    customer_name = models.CharField(max_length=250)
    customer_type = models.CharField(max_length=250)
    spoc_name = models.CharField(max_length=250, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='customer_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='customer_modified_by', db_column='modified_by', blank=True, null=True)
    is_active = models.BooleanField(default=True)


class CustomerAddress(models.Model):
    customer_address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    pin_code = models.BigIntegerField()
    seconde_line_address = models.CharField(
        max_length=250, blank=True, null=True)
    first_line_address = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='customer_address_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='customer_address_modified_by', db_column='modified_by', blank=True, null=True)
    is_active = models.BooleanField(default=True)
