from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    email = models.EmailField(max_length=254,verbose_name="email",unique=True)
    phone = models.CharField(max_length=50,verbose_name="phone")
class login(models.Model):
    email = models.ForeignKey(registration,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    email = models.ForeignKey(registration,on_delete=models.CASCADE)
    address = models.TextField(null=True)
    city = models.CharField(max_length=50 ,null=True)
    pincode = models.IntegerField(null=True)
