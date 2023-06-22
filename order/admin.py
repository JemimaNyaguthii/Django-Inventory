from django.contrib import admin

# Register your models here.
from.models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("customer_name","total_amount","order_date","is_completed")
admin.site.register(Order, OrderAdmin)
