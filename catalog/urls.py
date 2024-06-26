from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('catagory/<int:cat>', views.products_category, name='products_category'),
    path('catalog/<int:pk>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact')
]
