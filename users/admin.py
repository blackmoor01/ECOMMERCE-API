from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'phone_number', 'role', 'is_staff', 'is_active')  # Fields shown in the list
    search_fields = ('username', 'email', 'phone_number')  # Enable search functionality
    list_filter = ('role', 'is_staff', 'is_active')  # Add filter options

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'role', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'role'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
