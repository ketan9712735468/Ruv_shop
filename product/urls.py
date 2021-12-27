from django.urls import path
from product.views import Product

urlpatterns = [
    path('product_list/',Product.as_view(),name='product_list')
]