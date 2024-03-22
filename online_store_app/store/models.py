from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify


class Collection(models.Model):
    NAME_MAX_LENGTH = 125

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    featured_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()


class Product(models.Model):
    NAME_MAX_LENGTH = 125
    PRICE_MIN_VALUE = 1
    PRICE_MAX_DIGITS = 6
    PRICE_DECIMAL_PLACES = 2

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ],
    )

    inventory = models.PositiveIntegerField()

    # TODO: Fix this
    slug = models.SlugField(
        # unique=True,
        blank=True,
        editable=False,
    )

    last_update = models.DateTimeField(
        auto_now=True,
    )

    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT,
    )

    promotions = models.ManyToManyField(
        Promotion,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'price']


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

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return ' '.join([self.first_name, self.last_name])

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['first_name', 'last_name']


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
    )


class OrderItem(models.Model):
    PRICE_MIN_VALUE = 1
    PRICE_MAX_DIGITS = 6
    PRICE_DECIMAL_PLACES = 2

    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

    quantity = models.PositiveSmallIntegerField()

    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ],
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
    )


class Cart(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveSmallIntegerField()
