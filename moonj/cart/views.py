from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import product,cart
from registration.models import registration,login,Address
from registration.views import login1
# Create your views here.
class dash_product():
    def __init__(self,product_name,product_id,price,quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity =quantity
    

class cart_object():
    def __init__(self,product_name,product_id,price,quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity =quantity
def dashboard(request):
    object_list = []
    try:
        data = product.objects.all()[:3]
    except:
        print("not loaded")
    else:
        for x in data:
            ob = dash_product(x.product_name,x.product_id,x.price,x.quantity)
            #print(x.category_id.category_name)
            object_list.append(ob)
    context ={
        "data":object_list
    }
    # if request.session.has_key('user_login_uesr_id'):
    #     return render
     #return render
    return HttpResponse("hello")
def cart1(request):
    object_list = []

    if request.session.has_key('user_login_uesr_id') and request.POST.get("show_cart"):
        user_id = request.session['user_login_user_id']
        data = registration.objects.get(email= user_id)
        data1 = cart.objects.filter(email=data)
        
        print(data1)
        for x in data1:

            prod = product.objects.get(product_id = x.product_id.product_id)
            #print(prod.product_name)
            ob = cart_object(prod.product_name,prod.product_id,prod.price,x.quantity)
            object_list.append(ob)
        context ={
            "data":object_list
        }
        #print(object_list)
        return render()
    return render()
def add_to_cart(request):
    if request.session.has_key('user_login_uesr_id') and request.GET.get("add_to_cart"):
        quantity = 1
        product_id = request.GET.get('product_id')
        user_id = request.session['user_login_user_id']
        data = cart(email = user_id,product_id=product_id,quantity=quantity)
        data.save()
def remove_from_cart(request):
    if request.session.has_key('user_login_user_id') and request.GET.get("remove_from_cart"):
        user_id= request.session['user_login_user_id']
        product_transaction_id = request.session.cart_product_id
        data_obj = cart.objects.get(product_transaction_id=product_transaction_id)
        data_obj.delete()
    return redirect('login/')
def checkout(request):
    #if request.session.has_key('user_login_user_id') and request.GET.get("checkout"):
        user_id = "rmekamal789@gmail.com"#request.session.has_key('user_login_user_id')
        data = registration.objects.get(email =user_id)
        cart_data = cart.objects.filter(email= data)
        total_price = 0
        for x in cart_data:
           product_id = x.product_id.product_id;
           price = int(product.objects.get(product_id=product_id).price)
           total_price= total_price+price
        return HttpResponse(total_price)

