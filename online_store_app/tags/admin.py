from django.contrib import admin

from online_store_app.tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']
