from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.CustomerSerializer):
    class Meta:
        model=Customer
        fiels="__all__"