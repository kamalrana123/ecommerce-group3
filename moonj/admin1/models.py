from django.db import models

class admin_login(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
