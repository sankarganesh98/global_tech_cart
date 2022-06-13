from django.urls import path
from knox import views as knox_views
from .views import ProductMasterView, ProductMasterDetailView, GroupMasterView, GroupMasterDetailView, ProductCategoryView, ProductCategoryDetailView

urlpatterns = [
    path('product/', ProductMasterView.as_view(), name='productMaster'),
    path('product/<int:pk>/', ProductMasterDetailView.as_view(),
         name='product-detail'),
    path('group/', GroupMasterView.as_view(), name='productMaster'),
    path('group/<int:pk>/', GroupMasterDetailView.as_view(),
         name='product-detail'),
    path('category/', ProductCategoryView.as_view(), name='productMaster'),
    path('category/<int:pk>/', ProductCategoryDetailView.as_view(),
         name='product-detail'),
]
