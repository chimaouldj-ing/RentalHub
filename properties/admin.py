from django.contrib import admin
from django.utils.html import format_html

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "image_preview",
        "title",
        "city",
        "price",
        "rooms",
        "surface",
        "available",
        "created_at",
    )

    list_filter = (
        "city",
        "available",
        "rooms",
    )

    search_fields = (
        "title",
        "city",
        "address",
        "description",
    )

    ordering = ("-created_at",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="70" '
                'style="object-fit: cover; border-radius: 8px;" />',
                obj.image.url
            )

        return "No image"

    image_preview.short_description = "Image"