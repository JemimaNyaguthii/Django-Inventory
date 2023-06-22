from django.db import models

# Create your models here.
class ShoppingCart(models.Model):
    customer_name = models.CharField(max_length=255)
    current_date = models.DateTimeField(auto_now_add=True)
    products = models.JSONField()
    total_price = models.FloatField()
