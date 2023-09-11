from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.CustomerSerializer):
    class Meta:
        model=Customer
        fiels="__all__"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class CartSerializer(serializers.ModelSerializer):
    products =ProductSerializer(many =True)
    class Meta:
        model = Cart
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        