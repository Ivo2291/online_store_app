from django.db import models


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

    last_update = models.DateTimeField(
        auto_now=True,
    )


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


class Address(models.Model):
    STREET_MAX_LENGTH = 155
    CITY_MAX_LENGTH = 55

    street = models.CharField(
        max_length=STREET_MAX_LENGTH,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
    )

    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
