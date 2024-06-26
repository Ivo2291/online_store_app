# Generated by Django 5.0.3 on 2024-04-03 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.size')),
            ],
        ),
    ]
