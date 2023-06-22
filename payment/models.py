from django.db import models

# Create your models here.
class Payment(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date_payed= models.DateTimeField(null=True, blank=True)
   
