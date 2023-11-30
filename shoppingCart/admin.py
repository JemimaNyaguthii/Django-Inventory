from django.contrib import admin

# Register your models here.
from.models import Cart
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display=("customer_name","products","current_date","total_price")
admin.site.register(Cart, ShoppingCartAdmin)
