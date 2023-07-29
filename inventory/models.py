from django.db import models
from vendor.models import Vendor
# Create your models here.

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, null = True, on_delete = models.CASCADE)
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image=models.ImageField()
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
# All ->returns all intstances of a model
# filter->returns a subset of the data
# product.object.filter(price_ _lte=100)
# get returns a single object otherwise it returns an error