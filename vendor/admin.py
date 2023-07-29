from django.contrib import admin

# Register your models here.
from.models import Vendor
class VendorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone_number','email','address','order_number','order_date','is_completed')
admin.site.register(Vendor, VendorAdmin)
