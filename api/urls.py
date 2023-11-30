from django.urls import path
from .views import (
    CustomerListView,
    CustomerDetailView,
    CartListView,
    AddToCartView,
)

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:id>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('add_to_cart/', AddToCartView.as_view(), name='add-to-cart'),
]
