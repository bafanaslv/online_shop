from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (CategoryProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, ContactViews, ProductListView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('category/<int:category>', CategoryProductListView.as_view(), name='products_category'),
    path('category/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('category/create/', ProductCreateView.as_view(), name='product_create'),
    path('category/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('category/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contact/', ContactViews.as_view(), name='contact')
]
