from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('category/<int:category>', views.CategoryProductListView.as_view(), name='products_category'),
    path('category/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('category/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('category/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('contact/', views.contact, name='contact')
]
