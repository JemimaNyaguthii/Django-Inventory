from django.urls import path
from.views import products_list, product_detail, product_upload_view,product_update_view


urlpatterns=[
    path("products/upload",product_upload_view,name="product_upload_view"),
    path("products/list",products_list,name="products_list_view"),
    path("products/<int:id>",product_detail,name="product_detail_view"),
    path("products/edit/<int:id>",product_update_view,name="product_update"),

]
