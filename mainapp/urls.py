from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    path('', views.product_list, name='product_list'),
   
    path('manufacturers/dashboard', views.manufacturers, name = 'd_manu'),
    path('customers/liqours/', views.customers, name = 'cust_liq'),
    path('signup/', views.signup, name = 'all_signup'),
    path('decider/', views.decider, name = 'udecider'),
    path('liquor/<int:pk>/', views.liquor, name='liquor'),
    path('seller/dashboard', views.sellers, name = 'd_seller'),
    path('seller/order', views.seller_order, name = 's_orders'),
    path('seller/history',views.seller_history, name='s_history'),
    path('seller/stock',views.seller_stock, name='s_stock'),

    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)