from django.db import models

class Vendor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    order_number = models.CharField(max_length=50)
    order_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='vendor_images/', default='default_vendor_image.png')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
  

   



