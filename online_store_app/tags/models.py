from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    LABEL_MAX_LENGTH = 155

    label = models.CharField(
        max_length=LABEL_MAX_LENGTH,
    )

    def __str__(self):
        return self.label


class TaggedItem(models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey()
