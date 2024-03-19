from django.db import models
from django.template.defaultfilters import slugify


class Collection(models.Model):
    TITLE_MAX_LENGTH = 125

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    featured_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )


class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()


class Product(models.Model):
    TITLE_MAX_LENGTH = 125
    PRICE_MAX_DIGITS = 6
    PRICE_DECIMAL_PLACES = 2

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
    )

    inventory = models.IntegerField()

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    last_update = models.DateTimeField(
        auto_now=True,
    )

    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT,
        related_name='products',
    )

    promotions = models.ManyToManyField(
        Promotion,
        related_name='products',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')

        return super().save(*args, **kwargs)


class Customer(models.Model):
    FIRST_NAME_MAX_LENGTH = 35
    LAST_NAME_MAX_LENGTH = 45
    PHONE_MAX_LENGTH = 25
    MEMBERSHIP_MAX_LENGTH = 1

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    email = models.EmailField(
        unique=True,
    )

    phone = models.CharField(
        max_length=PHONE_MAX_LENGTH,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    membership = models.CharField(
        max_length=MEMBERSHIP_MAX_LENGTH,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE,
    )


class Order(models.Model):
    PAYMENT_STATUS_MAX_LENGTH = 1

    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(
        auto_now_add=True,
    )

    payment_status = models.CharField(
        max_length=PAYMENT_STATUS_MAX_LENGTH,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='orders',
    )


class OrderItem(models.Model):
    UNIT_PRICE_MAX_DIGITS = 6
    UNIT_PRICE_DECIMAL_PLACES = 2

    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='order_items',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='order_items',
    )

    quantity = models.PositiveSmallIntegerField()

    price = models.DecimalField(
        max_digits=UNIT_PRICE_MAX_DIGITS,
        decimal_places=UNIT_PRICE_DECIMAL_PLACES,
    )


class Address(models.Model):
    STREET_MAX_LENGTH = 155
    CITY_MAX_LENGTH = 55

    street = models.CharField(
        max_length=STREET_MAX_LENGTH,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='addresses',
    )


class Cart(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='cart_items',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='cart_items',
    )

    quantity = models.PositiveSmallIntegerField()
