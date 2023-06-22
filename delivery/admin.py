from django.contrib import admin

# Register your models here.
from.models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display=('status','delivery_address','delivery_date','delivery_person')

admin.site.register(Delivery,DeliveryAdmin)