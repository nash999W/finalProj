from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'image', 'predicted_result')
    search_fields = ('title', 'body', 'predicted_result')
    list_filter = ('predicted_result',)  # optional: add filters based on your needs
    fields = ('title', 'body', 'image', 'predicted_result')  # fields to be displayed and edited in the admin form
