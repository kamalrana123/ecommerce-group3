from django.db import models
from registration.models import registration
# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=50)
    category_id = models.AutoField(primary_key=True)
class product(models.Model):
    product_name = models.CharField(max_length=500)
    product_id = models.AutoField(primary_key=True)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(category,on_delete=models.CASCADE)
    price = models.IntegerField()

class cart(models.Model):
    product_transaction_id = models.AutoField(primary_key=True)
    email = models.ForeignKey(registration,on_delete=models.CASCADE)
    product_id = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
class trasaction(models.Model):
    trasaction_id = models.AutoField(primary_key=True)
    email = models.ForeignKey(registration,on_delete=models.CASCADE)
    product_transaction_id = models.ForeignKey(cart,on_delete=models.CASCADE)
    status = models.IntegerField()