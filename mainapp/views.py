from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from mainapp.models import ManuProducts, SellOrders,User, Products, Brands
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .decorators import customer_required
from .decorators import seller_required
from .decorators import manufacturer_required
from django.contrib.auth.decorators import login_required
from .forms import CustomerSignUpForm
from .forms import SellerSignUpForm
from .forms import ManufacturerSignUpForm

def decider(request):
    if request.user.is_customer:
        return redirect('cust_liq')
    elif request.user.is_seller:
        return redirect('d_seller')
    elif request.user.is_manufacturer:
        return redirect('d_manu')

    return render(request,'home.html',{})

def signup(request):
    return render(request,'signup.html',{})  
   
def product_list(request):
    liquors = Products.objects.all()
    brands = Brands.objects.all()
    hotproducts = Brands.objects.order_by("created_date")[:4]
    context = {'brands': brands,
    'liquors':liquors,
    'hotproducts':hotproducts}

    return render(request,'home.html',context)
@login_required
@manufacturer_required
def manufacturers(request):
    # logics and data loads
    return render(request, 'manufacturers.html',{})

@login_required
@seller_required
def sellers(request):
    liquors = Products.objects.all()
    brands = ManuProducts.objects.all()
    stocks = ManuProducts.objects.order_by("created_date")[:4]
    context = {
        'brands': brands,
        'liquors':liquors,
        'stocks':stocks
        }


    return render(request,'sellers.html',context)   


@login_required
@customer_required
def customers(request):
    liquors = Products.objects.all()
    brands = Brands.objects.all()
    context = {'brands': brands,
    'liquors':liquors,
    }
    return render(request, 'liquors.html',context) 

@login_required
@customer_required
def liquor(request,pk):
    # liquors = ManuProducts.objects.all()
    # ManuProducts.objects.get(pk=pk)
    liquor = get_object_or_404(Brands, pk=pk)
    liquors = Products.objects.order_by("id")[:3]
    brands = Brands.objects.all()
    context = {'brands': brands,
    'liquors':liquors,
    'liquor':liquor
    }
    
    return render(request, 'liquor.html',context)  

# def liquor(request):
#     liquors = ManuProducts.objects.all()
#     return render(request,'liquor.html',{'liquors':liquors}) 

def seller_order(request):
    orders = SellOrders.objects.all()
    return render(request, 's_orders.html',{'orders':orders})

def seller_history(request):
    return render(request, 's_history.html',{}) 

def seller_stock(request):
    return render(request, 's_stock.html',{})         




class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Registration Success! Enjoy your shoping')
        return redirect('cust_liq')  
     

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('d_seller')        

class ManufacturerSignUpView(CreateView):
    model = User
    form_class = ManufacturerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manufacturer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('d_manu')        