from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'author', 'status', 'published_at', 'created_at'
    list_editable = 'status',
    autocomplete_fields = 'author',
