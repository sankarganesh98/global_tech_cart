from django.db import models
from django.contrib.auth.models import User
from enterprise.models import Enterprise
from product.models import ProductMaster


# Create your models here.
class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductMaster, models.DO_NOTHING)
    group_id = models.IntegerField()
    enterprise = models.ForeignKey(Enterprise, models.DO_NOTHING)
    warehouse_id = models.IntegerField()
    batch_number = models.CharField(max_length=250)
    quantity = models.BigIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='inventory_created_by', db_column='created_by', blank=True, null=True)
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, related_name='inventory_modified_by', db_column='modified_by', blank=True, null=True)
    is_active = models.BooleanField(default=True)
