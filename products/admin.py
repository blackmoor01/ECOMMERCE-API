from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')  # Columns in the admin list view
    search_fields = ('name', 'description')  # Enable search by name and description
    list_filter = ('price', 'stock', 'created_at')  # Filters on the sidebar
    ordering = ('-created_at',)  # Default ordering (latest products first)
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only

    fieldsets = (
        ('Basic Information', {'fields': ('name', 'description')}),
        ('Pricing & Stock', {'fields': ('price', 'stock')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )

admin.site.register(Product, ProductAdmin)
