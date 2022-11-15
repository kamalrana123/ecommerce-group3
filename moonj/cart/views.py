from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import product,cart
from registration.models import registration,login,Address
from registration.views import login1
from datetime import datetime
# Create your views here.


class dash_product():
    def __init__(self,product_name,product_id,price,quantity,img):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity =quantity
        self.img=img
    

class cart_object():
    def __init__(self,product_name,product_id,price,quantity,img):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity =quantity
        self.img = img


def dashboard(request):
    object_list = []
    # if request.session.has_key('user_login_uesr_id'):
    #     return render
     #return render
    if request.GET.get('pk')=="2":
        try:
            data = product.objects.all()[:9]
        except:
            print("not loaded")
        else:
            for x in data:
                ob = dash_product(x.product_name,x.product_id,x.price,x.quantity,x.image)
                print(ob.img.url)
                object_list.append(ob)
        context ={
        "data":object_list
        }
        return render(request,'registeration/product.html',context)
    try:
        data = product.objects.all()[:3]
    except:
        print("not loaded")
    else:
        for x in data:
            ob = dash_product(x.product_name,x.product_id,x.price,x.quantity,x.image)
            print(ob.img.url)
            object_list.append(ob)
    context ={
        "data":object_list
    }
    return render(request,'registeration/product.html',context)


def cart1(request):
    object_list = []
    
    if request.session.has_key('user_login_uesr_id') and request.POST.get("show_cart"):
        user_id = request.session['user_login_user_id']
        data = registration.objects.get(email= user_id)
        data1 = cart.objects.filter(email=data)
        
        print(data1)
        for x in data1:

            prod = product.objects.get(product_id = x.product_id.product_id)
            print(prod.product_name)
            ob = cart_object(prod.product_name,prod.product_id,prod.price,x.quantity,x.image)
            print(prod.image)           
            object_list.append(ob)
        context ={
            "data":object_list
        }
        #print(object_list)
        return render()
    return render()


def add_to_cart(request):
    print(request.session['user_login_user_id'])
    print(request.GET.get('productid'))
    if request.session.has_key('user_login_user_id') and request.GET.get('productid')!="":
        print("hello")
        quantity = 1
        objtime = datetime.now().time()
        product_id = request.GET.get('productid')
        print(product_id)
        product_obj = product.objects.get(product_id=product_id)

        user_id = request.session['user_login_user_id']
        user_obj = registration.objects.get(email=user_id)

        data = cart(email = user_obj,product_id=product_obj,quantity=quantity,time=objtime)
        data.save()
    return HttpResponse("hello")


def remove_from_cart(request):
    if request.session.has_key('user_login_user_id') and request.GET.get("remove_from_cart"):
        user_id= request.session['user_login_user_id']
        product_transaction_id = request.session.cart_product_id
        data_obj = cart.objects.get(product_transaction_id=product_transaction_id)
        data_obj.delete()
    return redirect('login/')
def checkout(request):
    if request.session.has_key('user_login_user_id') and request.GET.get("checkout"):
        user_id = request.session['user_login_user_id']
        data = registration.objects.get(email =user_id)
        cart_data = cart.objects.filter(email= data)
        total_price = 0
        for x in cart_data:
           product_id = x.product_id.product_id;
           price = int(product.objects.get(product_id=product_id).price)
           total_price= total_price+(price*x.quantity)
        return HttpResponse(total_price)

