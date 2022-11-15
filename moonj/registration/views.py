from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import registration,login,Address
def logi(request):
    return render(request,'registeration/navbar.html')
def logout(request):
    try:
        del request.session['user_login_user_id']
    except:
        pass
    else:
        return redirect('login1')
def signup(request):
    if request.session.has_key('user_login_user_id'):
        return redirect('logout')
    if request.method == 'POST' and request.POST.get('signup'):
        name  = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        try:
            data = registration.objects.get(email=email)
        except:
            NewUserObject = registration(name = name, email = email,phone = phone)
            NewUserObject.save()
            data = registration.objects.get(email=email);
            NewLoginObject = login(email=data,password=password)
            NewLoginObject.save()
            context = {
                "msg":"successfully",
            }
            return render(request,'login1',context)
        else:
            context ={
                "msg":"user already exists",
            }
        return render(request,signup.html,context)
def login1(request):
    print("hello")
    
    #return HttpResponse("hello")
    try:
        del request.session['user_login_user_id']
    except:
        pass
    if not request.session.has_key('user_login_user_id'):
        print("hello")
        return render(request,'registeration/login.html',{})
    # if request.session.has_key('user_login_user_id'):
    #     context = {
    #         "user_id":request.session['user_login_user_id'],
    #     }
    #     return 
    # if request.methos == 'POST' and request.POST.get('login'):
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     try:
    #         data = registration.objects.get(email=email)    
    #     except:
    #         print("user not found")
    #     else:
    #         password = str(login.objects.get(email=data).password)
    #         usdp=str(request.POST.get('password'))
    #         if  usdp == password:
    #             #login success
    #             request.session['user_login_user_id'] = email
    #             print("logged in")
    #             context={
    #                 "user_id":email,
    #             }
    #             return render(request, dashboard.html, context)
    #         else:
    #             context={
    #                 "msg":"password not correct",
    #             }
    #             return render(request,login.html,context)
    #    return render(request,login.html)
    return HttpResponse("hello world")
class user_profile():
    def __init__(self,user_name,email,phone):
        self.user_name=user_name
        self.email=email
        self.phone=phone
def profile(request):
    if request.session.has_key('user_login_user_id') and request.GET.get('viewProfile'):
        user_id = request.session['user_login_user_id']
        try:
            data = registration.objects.get(email=user_id)
        except:
            print("can not load")
        else:
            ob = user_profile(data.name,data.email,data.phone)
        context = {
            "data":ob,
        }
        #print(ob.user_name)
        
    if request.session.has_key('user_login_user_id') and request.GET.get('updateProfile'):
        user_id = request.session['user_login_user_id']
        name = "kamlu" #request.GET.get('name')
        phone= "8191008733" #request.GET.get('phone')
        data = registration.objects.get(email=user_id)
        data.name =name
        data.phone =phone
        data.save()
        return HttpResponse("")
class address_obj():
    def __init__(self,address,city,pincode,address_id):
        self.address = address
        self.city = city
        self.pincode = pincode
        self.address_id = address_id

def add_new_address(request):
    if request.session.has_key('user_login_user_id') and request.GET.get('add_new_address'):
        user_id = request.session('user_login_user_id')
        description = request.GET.get('description')
        city = request.GET.get('city')
        pincode = request.GET.get('pincode')
        data = registration.objects.get(email =user_id)
        new_address_object = Address(email=data,address= description,city=city,pincode=pincode)
        new_address_object.save()
        return HttpResponse("hello")
def changeAddress(request):
    if request.session.has_key('user_login_uesr_id') and request.GET.get('updateaddress'):
        address = request.GET.get('address')
        city = request.GET.get('city')
        pincode = request.GET.get('pincode')
        address_id = request.GET.get('address_id')
        data_obj = Address.objects.get(address_id=address_id)
        
        data_obj.address=address
        data_obj.city =city
        data_obj.pincode =pincode

        data_obj.save()
    if request.session.has_key('user_login_user_id'):
        user_id = request.session['user_login_user_id']
        data1 = registration.objects.get(email =user_id)
        obj_list=[]
        data = Address.objects.filter(email=data1)
        for x in data:
            obj = address_obj(x.address,x.city,x.pincode)
            # print(x.address)
            obj_list.append(obj)
        context = {
            "data":obj_list,
        }
        return HttpResponse("hello")
#change password
def change_password(request):
    if request.session.has_key('user_login_user_id') and request.POST.get('changepassword'):
        user_id = request.session['user_login_user_id']
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        data = registration.objects.get(email= user_id)
        account_password = str(login.objects.get(email=data).password)
        if account_password == old_password:
            user = login.objects.get(email=data)
            user.password = new_password
            user.save()
            return redirect('logout')
        else:
            return render(request)
        
