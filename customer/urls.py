from django.urls import path
from customer.views import Profile, Register,Login

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name="register"),
    path('profile/',Profile.as_view(),name="profile")
]