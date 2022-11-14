from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    email = models.EmailField(max_length=254,verbose_name="email")
    phone = models.CharField(max_length=50,verbose_name="phone")
    address = models.TextField(null=True)
    city = models.CharField(max_length=50 ,null=True)
    pincode = models.IntegerField(null=True)
class login(models.Model):
    email = models.ForeignKey(registration,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)