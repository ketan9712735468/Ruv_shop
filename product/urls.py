from django.urls import path
from product.views import Product,Blog,About

urlpatterns = [
    path('product_list/',Product.as_view(),name='product_list'),
    path('blog/',Blog.as_view(),name="blog"),
    path('about/',About.as_view(),name="about")
]