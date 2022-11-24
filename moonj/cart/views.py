from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import product,cart,trasaction,user_orders,category
from registration.models import registration,login,Address
from registration.views import login1
from datetime import datetime
# Create your views here.

class user_data_object():
    def __init__(self,email,name):
        self.email = email
        self.name = name

class dash_product():
    def __init__(self,product_name,product_id,price,quantity,img):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity =quantity
        self.img=img
    

class cart_object():
    def __init__(self,product_name,product_id,price,quantity,img,product_transaction_id):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity =quantity
        self.img = img
        self.product_transaction_id =product_transaction_id


def dashboard(request):
    object_list = []
    # if request.session.has_key('user_login_uesr_id'):
    #     return render
     #return render
    user_obj = user_data_object("","")
    if request.session.has_key('user_login_user_id'):
        user_id= request.session['user_login_user_id']
        name = registration.objects.get(email=user_id).name
        user_obj = user_data_object(user_id,name)
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
        "data1":object_list,
        "data":user_obj
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
        "data1":object_list,
        "data":user_obj
    }
    return render(request,'registeration/product.html',context)


def cart1(request):
    object_list = []
    user_obj = user_data_object("","")
    if request.session.has_key('user_login_user_id'):
        user_id= request.session['user_login_user_id']
        name = registration.objects.get(email=user_id).name
        user_obj = user_data_object(user_id,name)
    if request.session.has_key('user_login_user_id'):
        user_id = request.session['user_login_user_id']
        data = registration.objects.get(email= user_id)
        data1 = cart.objects.filter(email=data).order_by('time').reverse()
        print(data1)
        for x in data1:

            prod = product.objects.get(product_id = x.product_id.product_id)
            print(prod.product_name)
            ob = cart_object(prod.product_name,prod.product_id,prod.price,x.quantity,prod.image,x.product_transaction_id)
            print(prod.image)           
            object_list.append(ob)
        context ={
            "data1":object_list,
            "data":user_obj,
        }
        #print(object_list)
        return render(request,'registeration/cart.html',context)
    return redirect('/login')


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
        return redirect('/cart')
    return redirect('/login')


def remove_from_cart(request):
    if request.session.has_key('user_login_user_id'):
        user_id= request.session['user_login_user_id']
        product_transaction_id = request.GET.get('id')
        try:
            data_obj = cart.objects.get(product_transaction_id=product_transaction_id)
        except:
            return redirect('/cart')
        else:
            data_obj.delete()
        return redirect('/cart')
    return redirect('/login')


def checkout(request):
    return render(request,'registeration/checkout.html')
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


class orders_users():
    def __init__(self,product_name,product_id,quantity, price,status,time,img):
        self.product_name =product_name
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.status = status
        self.time =time
        self.img =img
#creating orders of the users
def orders(request):
    object_list = []
    user_obj = user_data_object("","")
    if request.session.has_key('user_login_user_id'):
        user_id= request.session['user_login_user_id']
        name = registration.objects.get(email=user_id).name
        user_obj = user_data_object(user_id,name)
    if request.session.has_key('user_login_user_id'):
        user_id=request.session['user_login_user_id']
        data = registration.objects.get(email=user_id)
        data_obj = user_orders.objects.filter(email=data).order_by('time').reverse()
        for x in data_obj:
            product_id = x.product_id.product_id
            product_obj = product.objects.get(product_id=product_id)
            ob = orders_users(product_obj.product_name,product_obj.product_id,x.quantity,x.price,x.status,x.time,product_obj.image)
            object_list.append(ob)
            print(product_id)
        context={
            "data1":object_list,
            "data":user_obj,
        }
        print(object_list)
        return render(request,'registeration/orders.html',context)
    return redirect('/login')