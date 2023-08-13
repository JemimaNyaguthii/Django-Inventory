from django.urls import path
from .views import vendor_list
from .views import vendor_detail
from .views import upload_vendor
from .views import edit_vendor
from .views import delete_vendor

urlpatterns = [
    path("vendors/list/", vendor_list, name="vendor-list"),
    path("vendors/<int:pk>/", vendor_detail, name="vendor-detail"),
    path("vendors/upload/", upload_vendor, name="upload-vendor"),
    path("vendors/edit/<int:pk>/", edit_vendor, name="edit-vendor"),
    path("vendors/delete/<int:pk>/", delete_vendor, name="delete-vendor"),
]
