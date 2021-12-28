from django.urls import path
from product.views import Product,Blog

urlpatterns = [
    path('product_list/',Product.as_view(),name='product_list'),
    path('blog/',Blog.as_view(),name="blog")
]