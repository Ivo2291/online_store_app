from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from online_store_app.store.admin import ProductAdmin
from online_store_app.store.models import Product
from online_store_app.tags.models import TaggedItem


class TagInLine(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
    min_num = 1
    max_num = 10
    extra = 0


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]


admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
