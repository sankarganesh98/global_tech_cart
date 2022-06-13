from rest_framework.serializers import ModelSerializer
from .models import Customer, CustomerAddress


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAddressSerializer(ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'
