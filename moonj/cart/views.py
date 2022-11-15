from django.shortcuts import render
from django.http import HttpResponse 
from .models import product,cart
from registration.models import registration,login,Address
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
def checkout(request):
    pass
