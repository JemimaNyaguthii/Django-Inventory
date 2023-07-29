from django.db import models

# Create your models here.
class Delivery(models.Model):
    status = models.CharField(max_length=255)
    delivery_date = models.DateTimeField()
    delivery_address = models.CharField(max_length=255)
    delivery_person = models.CharField(max_length=255)
    customer_name=models.CharField(max_length=255)
