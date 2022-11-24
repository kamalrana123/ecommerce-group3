# Generated by Django 4.0.3 on 2022-11-16 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_remove_address_id_address_address_id_and_more'),
        ('cart', '0009_cart_time_trasaction_time_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('status', models.BooleanField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.registration')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.product')),
            ],
        ),
    ]