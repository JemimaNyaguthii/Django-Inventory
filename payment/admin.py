from django.contrib import admin

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=('name','amount','payment_method','date_payed','status')
admin.site.register(Payment, PaymentAdmin)
