from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from online_store_app.store.models import Collection, Product, Customer, Order, OrderItem


class InventoryFilter(admin.SimpleListFilter):
    LESS_THAN_10 = '<10'
    EMPTY = '=0'

    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            (self.LESS_THAN_10, 'Low'),
            (self.EMPTY, 'Empty'),
        ]

    def queryset(self, request, queryset):
        if self.value() == self.EMPTY:
            return queryset.filter(inventory=0)

        elif self.value() == self.LESS_THAN_10:
            return queryset.filter(inventory__lt=10)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                    'collection__id': str(collection.pk)
                }))

        return format_html('<a href="{}">{}</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request) \
            .annotate(products_count=Count('products'))


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    search_fields = ['name']
    list_display = ['name', 'price', 'inventory_status', 'collection_name']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_select_related = ['collection']
    list_editable = ['price']
    list_per_page = 10

    @staticmethod
    def collection_name(product):
        return product.collection.name

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory == 0:
            return 'EMPTY'
        elif product.inventory < 10:
            return 'LOW'

        return 'OK'

    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} successfully updated product(s).'
        )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    ordering = ['first_name', 'last_name']

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
                reverse('admin:store_order_changelist')
                + '?'
                + urlencode({
                    'customer__id': str(customer.pk)
                })
        )

        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )


class OrderItemInLine(admin.TabularInline):
    autocomplete_fields = ['product']
    model = OrderItem
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'placed_at', 'customer']
    inlines = [OrderItemInLine]
    autocomplete_fields = ['customer']
