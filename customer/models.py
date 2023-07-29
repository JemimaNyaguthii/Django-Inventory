from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=255,default='Unknown')
    address=models.CharField(max_length=20,default='Unknown')
    order_history=models.JSONField(null=True)

    def register(self):
        self.save

    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        

    def isExist(self):
        if Customer.objects.filter(email = self.email):
             return True
        
        return False




    
    
