from django.urls import path
from knox import views as knox_views
from .views import CustomerView, CustomerDetailView, CustomerAddressView, CustomerAddressDetailView

urlpatterns = [
    path('customer/', CustomerView.as_view(), name='customerMaster'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(),
         name='customer-detail'),
    path('customeraddress/', CustomerAddressView.as_view(), name='productMaster'),
    path('customeraddress/<int:pk>/', CustomerAddressDetailView.as_view(),
         name='customeraddress-detail'),
]
