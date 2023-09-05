urlpatterns = [ 
path('customers/', CustomerListView.as_view(), name='customer_list_view'), 
path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail_view'), 
]
