from django.db import models

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