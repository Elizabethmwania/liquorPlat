from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
app_name = 'cart'

urlpatterns = [
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('add/(?P<product_id>\d+)/', views.cart_add, name='cart_add'),
    path('remove/(?P<product_id>\d+)/', views.cart_remove, name='cart_remove'),
]