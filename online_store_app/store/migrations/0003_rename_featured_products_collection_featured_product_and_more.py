# Generated by Django 5.0.3 on 2024-03-19 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='featured_products',
            new_name='featured_product',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='unit_price',
            new_name='price',
        ),
    ]