# Generated by Django 4.0.3 on 2022-11-30 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trasaction',
            name='product_transaction_id',
        ),
    ]
