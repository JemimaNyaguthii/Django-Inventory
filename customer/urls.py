from django.urls import path
from. import views
urlpatterns = [
    path("customer/upload/",views.customer_upload_view, name = "customer_upload_view"),
    path("customer/list/",views.customer_list,name="customer_list_view"),
    path("customer/<int:id>/",views.customer_detail,name="customer_detail_view"),
    path("customer/edit/<int:id>/",views.customer_update_view,name="customer_update"),
    path("customer/delete/<int:id>/",views.delete_customer,name="customer_delete"),

    
]