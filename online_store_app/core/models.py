from django.db import models
from django.template.defaultfilters import slugify


class Banner(models.Model):
    IMAGE_MAX_LENGTH = 200
    ALT_TEXT_MAX_LENGTH = 300

    image = models.CharField(
        max_length=IMAGE_MAX_LENGTH,
    )

    alt_text = models.CharField(
        max_length=ALT_TEXT_MAX_LENGTH,
    )


class Category(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image = models.ImageField(upload_to='brand_images/')

    def __str__(self):
        return self.title


class Color(models.Model):
    TITLE_MAX_LENGTH = 100
    COLOR_CODE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    color_code = models.CharField(
        max_length=COLOR_CODE_MAX_LENGTH,
    )

    def __str__(self):
        return self.title


class Size(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image = models.ImageField(upload_to='product_images/')

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    in_stock = models.BooleanField(
        default=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products',
    )

    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name='products',
    )

    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name='products',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.id}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductAttribute(models.Model):
    price = models.PositiveIntegerField()

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_attributes',
    )

    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name='product_attributes',
    )

    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name='product_attributes',
    )

    def __str__(self):
        return self.product.title
