from django.urls import path
from blog.apps import BlogConfig
from blog import views

app_name = BlogConfig.name

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='confirm_delete'),
]
