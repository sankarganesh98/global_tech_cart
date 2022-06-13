from django.db import models
from django.contrib.auth.models import User
from enterprise.models import Enterprise

# Create your models here.
class ProductCategory(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
       User, models.DO_NOTHING, related_name='category_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='category_modified_by', db_column='modified_by', blank=True, null=True)
    is_active = models.BooleanField(default=True)



class ProductMaster(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_description = models.CharField(max_length=250)
    product_image = models.CharField(max_length=250, blank=True, null=True)
    product_category = models.ForeignKey(
        ProductCategory, models.DO_NOTHING, blank=True, null=True)
    barcode_number = models.BigIntegerField(blank=True, null=True)
    retail_price = models.BigIntegerField(blank=True, null=False)
    wholesale_price = models.BigIntegerField(blank=True, null=False)
    enterprise = models.ForeignKey(Enterprise, models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='product_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='product_modified_by', db_column='modified_by', blank=True, null=True)
    is_active = models.BooleanField(default=True)



class GroupMaster(models.Model):
    group_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    group_description = models.CharField(max_length=250)
    group_quantity = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='groups_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='groups_modified_by', db_column='modified_by', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    enterprise = models.ForeignKey(Enterprise, models.DO_NOTHING)

