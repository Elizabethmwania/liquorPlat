from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from mainapp.models import Customer, Seller, Manufacturer, User

class CustomerSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','phone_number','location','id_number','email','password1','password1',]
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user

class SellerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','seller_code','location','email','password1','password1',]
    

    @transaction.atomic 
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        seller = Seller.objects.create(user=user)
        return user        

class ManufacturerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','manufacturer_code','location','email','password1','password1',]
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manufacturer = True
        if commit:
            user.save()
        return user        