from rest_framework.serializers import ModelSerializer
from .models import Enterprise, EnterpriseAddress, Warehouse, WarehouseAddress


class EnterpriseSerializer(ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class EnterpriseAddressSerializer(ModelSerializer):
    class Meta:
        model = EnterpriseAddress
        fields = '__all__'


class WarehouseSerializer(ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseAddressSerializer(ModelSerializer):
    class Meta:
        model = WarehouseAddress
        fields = '__all__'
