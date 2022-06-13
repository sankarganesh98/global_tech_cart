from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Enterprise(models.Model):
    enterprise_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=250)
    phone_number = models.BigIntegerField()
    email_id = models.CharField(max_length=250)
    company_logo = models.CharField(max_length=250, blank=True, null=True)
    proprietor_name = models.CharField(max_length=250)
    proprietor_email = models.CharField(max_length=250)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='enterprise_created_by', db_column='created_by')
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='enterprise_modified_by', db_column='modified_by')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)

class EnterpriseAddress(models.Model):
    enterprise_address_id = models.AutoField(primary_key=True)
    enterprise = models.ForeignKey(Enterprise, models.DO_NOTHING)
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    pincode = models.BigIntegerField()
    second_line_address = models.CharField(
        max_length=250, blank=True, null=True)
    first_line_address = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    phone_number = models.BigIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='enterprise_address_created_by', db_column='created_by')
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='enterprise_address_modified_by', db_column='modified_by')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=250)
    enterprise = models.ForeignKey(Enterprise, models.DO_NOTHING)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='warehouse_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='warehouse_modified_by', db_column='modified_by', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)



class WarehouseAddress(models.Model):
    warehouse_address_id = models.AutoField(primary_key=True)
    warehouse = models.ForeignKey(Warehouse, models.DO_NOTHING)
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    pincode = models.BigIntegerField()
    second_line_address = models.CharField(
        max_length=250, blank=True, null=True)
    first_line_address = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    phone_number = models.BigIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='warehouse_address_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='warehouse_address_modified_by', db_column='modified_by', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)