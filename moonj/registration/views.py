from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import registration,login,Address
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import requests
import json



class user_data_object():
    def __init__(self,email,name):
        self.email = email
        self.name = name



def home(request):
    if not request.session.has_key('user_login_user_id'):
        return render(request,'registeration/navbar.html')
    user_id= request.session['user_login_user_id']
    try:
        data_obj = registration.objects.get(email=user_id)
    except:
        return redirect('/')
    else:
        user_obj = user_data_object(data_obj.email,data_obj.name )
        context={
            "data":user_obj,
        }
        return render(request,'registeration/navbar.html',context)

    


def contact(request):
    if not request.session.has_key('user_login_user_id'):
        return render(request,'registeration/contact.html')
    user_id= request.session['user_login_user_id']
    try:
        data_obj = registration.objects.get(email=user_id)
    except:
        return redirect('/contact')
    else:
        user_id= request.session['user_login_user_id']
        user_obj = user_data_object(data_obj.email,data_obj.name )
        context={
            "data":user_obj,
        }
        return render(request, 'registeration/contact.html',context)



def signup(request):
    print("hello")
    if request.session.has_key('user_login_user_id'):
        return redirect('logout')
    if request.method == 'POST' and request.POST.get('signup'):
        name  = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
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
            return redirect('/login')
        else:
            context ={
                "msg":"user already exists",
            }
    return render(request,'registeration/signup.html',{})




def login1(request):
 
    try:
        del request.session['user_login_user_id']
    except:
        pass
    if request.session.has_key('user_login_user_id'):
        context = {
            "user_id":request.session['user_login_user_id'],
        }
        return render(request,'',{})
    #print(request.method)
    #print(request.POST.get('login'))
    if request.method == 'POST' and request.POST.get('login'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        email.lower()
        try:
            data = registration.objects.get(email=email)    
        except:
            print("user not found")
        else:
            password = str(login.objects.get(email=data).password)
            usdp=str(request.POST.get('password'))
            if  check_password(usdp,password):
                #login success
                request.session['user_login_user_id'] = email
                print("logged in")
                context={
                    "user_id":email,
                }
                return redirect('/')
                #return render(request,'registeration/navbar.html', context)
            else:
                context={
                    "msg":"password not correct",
                }
                return redirect('/login')
        return render(request,'registeration/login.html')
    
    return render(request,'registeration/login.html',{})




def logout(request):
    try:
        del request.session['user_login_user_id']
    except:
        pass
    else:
        return redirect('/login')




class user_profile():
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone



def profile(request):
    if not request.session.has_key('user_login_user_id'):
        return redirect('/login')
    if request.session.has_key('user_login_user_id'):
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
        return render(request,'registeration/profile.html',context)
        
    


def change_profile(request):
    user_obj = user_profile("","","")
    if not request.session.has_key('user_login_user_id'):
        return redirect('/login')
    if request.session.has_key('user_login_user_id'):
        user_id= request.session['user_login_user_id']
        name = registration.objects.get(email=user_id).name
        phone = registration.objects.get(email=user_id).phone
        user_obj = user_profile(name,user_id,phone)
        context={
            "data":user_obj,
        } 
    if request.session.has_key('user_login_user_id') and request.GET.get('updateProfile'):
        user_id = request.session['user_login_user_id']
        name = request.GET.get('name')
        phone= request.GET.get('phone')
        data = registration.objects.get(email=user_id)
        data.name =name
        data.phone =phone
        data.save()
        return redirect('/profile')
    return render(request,'registeration/edit_profile.html',context)


class address_obj():
    def __init__(self,address,city,pincode,address_id):
        self.address = address
        self.city = city
        self.pincode = pincode
        self.address_id = address_id



def get_pin_code(pinc):
    endpoint="https://api.postalpincode.in/pincode/"
    pincode1 = pinc
    response = requests.get(endpoint+pincode1)
    pincode_information = json.loads(response.text)
    neccessary_information = pincode_information[0]['Status']
    if neccessary_information == "Success":
        return True
    else:
        return False



def get_state(pinc):
    endpoint="https://api.postalpincode.in/pincode/"
    pincode1 = pinc
    response = requests.get(endpoint+pincode1)
    pincode_information = json.loads(response.text)
    neccessary_information = pincode_information[0]['PostOffice'][0]['State']
    
    #print(neccessary_information)
    return str(neccessary_information)

def get_country(pinc):
    endpoint="https://api.postalpincode.in/pincode/"
    pincode1 = pinc
    response = requests.get(endpoint+pincode1)
    pincode_information = json.loads(response.text)
    neccessary_information = pincode_information[0]['PostOffice'][0]['Country']
    
    #print(neccessary_information)
    return str(neccessary_information)
def add_new_address(request):
    if not request.session.has_key('user_login_user_id'):
        return redirect('/login')
        pass

    print(request.GET.get('add_new_address'))
    if request.session.has_key('user_login_user_id') and request.GET.get('add_new_address'):
        user_id = request.session['user_login_user_id']
        flat = request.GET.get('flat')
        area = request.GET.get('area')
        city = request.GET.get('city')
        pincode = str(request.GET.get('pincode'))
        if get_pin_code(pincode):
            data = registration.objects.get(email =user_id)
            state = str(get_state(pincode))
            country= str(get_country(pincode))
            new_address_object = Address(email=data,flat= flat,area=area,city=city,pincode=pincode,state=state,country=country)
            new_address_object.save()
    return render(request,'registeration/New_Address.html',{})



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
    user_obj = user_data_object("","")
    if request.session.has_key('user_login_user_id'):
        user_id= request.session['user_login_user_id']
        name = registration.objects.get(email=user_id).name
        user_obj = user_data_object(user_id,name)
        context={
            "data":user_obj,
        }
    if request.session.has_key('user_login_user_id') and request.POST.get('changepassword'):
        user_id = request.session['user_login_user_id']
        old_password = str(request.POST.get('old_password'))
        new_password = str(request.POST.get('new_password'))
        data = registration.objects.get(email= user_id)
        account_password = str(login.objects.get(email=data).password)
        if check_password(old_password,account_password):
            user = login.objects.get(email=data)
            user.password = make_password(new_password)
            user.save()
            return redirect('/logout')
        else:
            return render(request)
    return render(request,'registeration/edit_password.html',context)
        
def logout(request):
    try:
        del request.session['user_login_user_id']
    except:
        pass
    else:
        return redirect('/login')