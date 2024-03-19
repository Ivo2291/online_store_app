from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    LABEL_MAX_LENGTH = 155

    label = models.CharField(
        max_length=LABEL_MAX_LENGTH,
    )


class TaggedItem(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='tagged_items',
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='tagged_items',
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey()
