from _decimal import Decimal
from rest_framework import serializers

from online_store_app.store.models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['pk', 'name', 'products_count']

    products_count = serializers.SerializerMethodField(method_name='count_products')

    @staticmethod
    def count_products(collection: Collection):
        result = collection.products.count()

        return result


class ProductSerializer(serializers.ModelSerializer):
    PRICE_TAX = Decimal(1.1)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'description', 'price', 'inventory', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        result = round(product.price * self.PRICE_TAX, 2)

        return result


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['pk', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        created_review = Review.objects.create(product_id=product_id, **validated_data)

        return created_review
