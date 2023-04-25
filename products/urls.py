from django.urls import path
from .views import (
    ProductListView, ProductDetailView, CategoryListView, CategoryDetailView,
    FileListView, FileDetailView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('products/<int:product_id>/files/', FileListView.as_view(), name='file_list'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
]
