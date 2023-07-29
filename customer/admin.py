from django.contrib import admin
# Register your models here.
from.models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","phone_number",'payment_method','address','order_history')

admin.site.register(Customer,CustomerAdmin)
