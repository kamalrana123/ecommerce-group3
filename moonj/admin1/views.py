from django.shortcuts import render
from cart.models import product,category
from .models import *

class cate():
    def __init__(self,category_id,category_name):
        self.category_id = category_id
        self.catefory_name = category_name 
def add_item(request):
    if request.session.has_key('admin_login_id'):
        data = category.objects.all()
        obj_list =[]
        for x in data:
            obj = cate(x.category_id,x.category_name)
            obj_list.append(obj)
        context = {
            "data":obj_list,
        }
    if request.session.has_key('admin_login_id') and request.GET.get('add_item'):
        product_name = request.GET.get('product_name')
        description = request.GET.get('description')
        quantity = request.GET.get('quantity')
        image = request.GET.get('image')
        category_id = request.GET.get('category_id')
        price = request.GET.get('price')
        obj = product(product_name = product_name,description=description,quantity=quantity,image=image,category_id=category_id,price = price)
        obj.save()

def update_product(request):
    if request.session.has_key('admin_login_id') and request.GET.get('update_product'):
        product_id = request.GET.get('product_id')
        #getting information from the user
        
        data_obj = product.objects.get(product_id=product_id)
        product_name = request.GET.get('product_name')
        description = request.GET.get('description')
        quantity = request.GET.get('quantity')
        image = request.GET.get('image')
        category_id = request.GET.get('category_id')
        price = request.GET.get('price')
        
        #updating information in objects

        data_obj.product_name = product_name
        data_obj.description = description
        data_obj.quantity = quantity
        data_obj.image = image
        data_obj.category_id = category_id
        data_obj.price =price

        #saving the object
        data_obj.save()
def add_category(request):
    
    if request.session.has_key('admin_login_id') and request.GET.get('add_category'):
        category_name = request.GET.get('category_name')
        obj = category(category_name=category_name)
        obj.save()
def update_category(request):
    if request.session.has_key('admin_login_id') and request.GET.get('update_category'):
        category_id = request.GET.get('category_id')
        obj = category.objects.get(category_id=category_id)
        category_name = request.GET.get('category_name')
        obj.category_name=category_name
        obj.save()

class profile():
    def __init__(self,user_id, name):
      self.user_id =user_id
      self.name =name
def viewProfile(request):
    if request.session.has_key('admin_login_id'):
        user_id = request.session.has_key('admin_login_id')
        user = admin_login.objects.get(user_id =user_id)
        obj = profile(user.user_id,user.name)

        context = {
            "data":obj,
        }

