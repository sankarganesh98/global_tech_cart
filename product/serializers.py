from rest_framework.serializers import ModelSerializer
from .models import ProductMaster
from .models import GroupMaster
from .models import ProductCategory


class ProductMasterSerializer(ModelSerializer):
    class Meta:
        model = ProductMaster
        fields = '__all__'


class GroupMasterSerializer(ModelSerializer):
    class Meta:
        model = GroupMaster
        fields = '__all__'


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = GroupMaster
        fields = '__all__'
