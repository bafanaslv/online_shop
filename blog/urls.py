from django.urls import path
from blog.apps import BlogConfig
from blog import views

app_name = BlogConfig.name

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    # path('category/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    # path('category/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    # path('category/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete')
]
