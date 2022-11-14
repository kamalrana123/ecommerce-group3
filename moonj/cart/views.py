from django.shortcuts import render
from .models import product
# Create your views here.
class dash_product():
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
        print()
    else:
        for x in data:
             ob = dash_product(x.product_name,x.product_id,x.price,x.quantity)
             object_list.append(ob)
    context ={
        "data":object_list
    }
    if request.session.has_key['user_login_user_id']:
        return render
    return render
def cart(request):
    pass