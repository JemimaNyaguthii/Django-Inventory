# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shoppingCart/', include('shoppingCart.urls')),  # Include the URLs from the 'cart' app
]
