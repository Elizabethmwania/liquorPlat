
from django.contrib import admin
from django.urls import path, include
 
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls')),
    path('', include('mainapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/customer/', views.CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/signup/seller/', views.SellerSignUpView.as_view(), name='seller_signup'),
    path('accounts/signup/manufacturer/', views.ManufacturerSignUpView.as_view(), name='manufacturer_signup'),

]
