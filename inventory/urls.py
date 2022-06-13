from django.urls import path
from knox import views as knox_views
from .views import InventoryView, InventoryDetailView

urlpatterns = [
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(),
         name='Inventory-detail'),

]
