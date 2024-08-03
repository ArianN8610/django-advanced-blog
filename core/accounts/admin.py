from .models import User, Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = 'email', 'is_active', 'is_staff', 'is_superuser'
    list_filter = 'is_active', 'is_staff', 'is_superuser'
    search_fields = 'email',
    ordering = 'email',
    fieldsets = (
        ('Authentication', {
            'fields': ('email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Group permissions', {
            'fields': ('user_permissions', 'groups')
        }),
        ('Important dates', {
            'fields': ('last_login',)
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'user_permissions',
                'groups'),
        }),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = 'user',
