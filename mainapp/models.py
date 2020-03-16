import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_manufacturer = models.BooleanField(default=False)
    phone_number = models.IntegerField(blank=True,null=True)
    location = models.CharField(max_length=200,null=True)
    id_number = models.IntegerField(blank=True,null=True)
    seller_code = models.IntegerField(blank=True,null=True)
    manufacturer_code = models.IntegerField(blank=True,null=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Manufacturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Products(models.Model):
    name = models.CharField(max_length=200)
    


    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True,)
    created_date = models.DateTimeField(default=timezone.now)
    is_instock = models.BooleanField(default= True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(null=True, upload_to='media')

    def __str__(self):
        return self.name        




class ManuProducts(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    is_instock = models.BooleanField(default= True)
    img = models.ImageField(upload_to='media')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True) 
    
    def __str__(self):
        return self.name


class SellOrders(models.Model):
    item = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    status = models.DateTimeField()
    time = models.DateTimeField(default=timezone.now)
    is_delivered = models.BooleanField(default= True)
    

    def __str__(self):
        return self.item + str(self.id)
