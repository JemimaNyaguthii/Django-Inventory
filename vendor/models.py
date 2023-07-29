from django.db import models

# Create your models here.
class Vendor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    order_number = models.CharField(max_length=50)
    order_date = models.DateField()
    is_completed = models.BooleanField(default=False)

   



