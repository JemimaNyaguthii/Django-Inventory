from django.db import models
from inventory.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    items_name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    number_of_items=models.PositiveIntegerField(default=1)
    discount=models.DecimalField(max_digits=8,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    description=models.TextField()
    products=models.ManyToManyField(Product)

    def add_product(self,product):
        self.products.add(product)
        self.save()
        return self
    def get_total(self):
        products = self.products.all()
        total = 0
        for product in products:
            total+=product.price
        return total
