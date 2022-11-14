from django.shortcuts import render
from .models import *
def signup(request):
    if request.method == 'POST' and request.POST.get('signup'):
        name  = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        try:
            data = registration.objects.get(email=email)
        except:
            NewUserObject = registration(name = name, email = email,password=password,phone = phone)
            NewUserObject.save()
        else:
            context ={
                "msg":"user already exists"
            }
            return render(request,signup.html,context)
def login(request):
    if request.session.has_key['user_login_user_id']:
        context = {
            "user_id":request.session['user_login_user_id']
        }
        return 
    if request.methos == 'POST' and request.POST.get('login'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            data = login.objects.get(email=email)
        except:
            print("user not found")
        else:
            password = str(login.object.get(email=email).password)
            if str(request.POST.get()) == password:
                #login success
                request.session['user_login_user_id'] = email

                context={
                    "user_id":email
                }
                return render(request, dashboard.html, context)
            else:
                context={
                    "msg":"password not correct"
                }
                return render(request,login.html,context)
        return render(request,login.html)