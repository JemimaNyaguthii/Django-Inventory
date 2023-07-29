from django.db import models
from customer.models import Customer
from shoppingCart.models import ShoppingCart
from delivery.models import Delivery
# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    is_completed = models.BooleanField(default=False)


    customer = models.ForeignKey(Customer, null= True, on_delete = models.CASCADE)
    shoppingCart = models.ForeignKey(ShoppingCart, null= True, on_delete = models.CASCADE)
    delivery = models.OneToOneField(Delivery, null= True, on_delete=models.CASCADE)



    
