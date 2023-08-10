from django.contrib import admin
from.models  import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","stock","price","image","description","date_created","date_updated")

admin.site.register(Product,ProductAdmin)