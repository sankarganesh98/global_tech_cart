from django.urls import path
from .views import EnterpriseView, EnterpriseDetailView, EnterpriseAddressView, EnterpriseAddressDetailView, WarehouseView, WarehouseDetailView, WarehouseAddressView, WarehouseAddressDetailView

urlpatterns = [
    path('enterprise/', EnterpriseView.as_view(), name='enterprise'),
    path('enterprise/<int:pk>/', EnterpriseDetailView.as_view(),
         name='enterprise-detail'),
    path('enterpriseaddress/', EnterpriseAddressView.as_view(),
         name='enterprise-address'),
    path('enterprise/<int:pk>/', EnterpriseAddressDetailView.as_view(),
         name='enterprise-address-detail'),
    path('warehouse/', WarehouseView.as_view(), name='warehouse'),
    path('warehouse/<int:pk>/', WarehouseDetailView.as_view(),
         name='warehouse-detail'),
    path('warehouse/', WarehouseAddressView.as_view(), name='warehouse'),
    path('warehouse/<int:pk>/', WarehouseAddressDetailView.as_view(),
         name='warehouse-detail'),
]
