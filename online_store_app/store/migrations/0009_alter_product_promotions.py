# Generated by Django 5.0.3 on 2024-03-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_address_customer_alter_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, null=True, to='store.promotion'),
        ),
    ]