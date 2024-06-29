from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('category/<int:category>', views.CategoryProductListView.as_view(), name='products_category'),
    path('catalog/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('contact/', views.contact, name='contact')
]
