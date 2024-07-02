from django.urls import path
from blog.apps import BlogConfig
from blog import views

app_name = BlogConfig.name

urlpatterns = [
    path('', views.BlogListView.as_view(), name='list'),
    path('publish_true/', views.PublishTrueBlogListView.as_view(), name='publish_true'),
    path('publish_false/', views.PublishFalseBlogListView.as_view(), name='publish_false'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', views.BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='conform_delete'),
]
