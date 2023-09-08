from django.contrib import admin
from .models import Book, Genre

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'genre',
        'price',
        'image',
    )

    ordering = ('sku',)

class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)