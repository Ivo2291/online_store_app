from django.contrib import admin

from online_store_app.core.models import Category, Brand, Color, Size, Product, ProductAttribute


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'brand',
        'in_stock',
    ]

    list_editable = [
        'in_stock',
    ]


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product',
        'price',
        'color',
        'size',
    ]
