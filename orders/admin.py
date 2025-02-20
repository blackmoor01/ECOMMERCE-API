from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'created_at')  # Columns in the admin list view
    search_fields = ('user__username', 'product__name')  # Enable search by user and product name
    list_filter = ('created_at', 'total_price')  # Filters on the sidebar
    ordering = ('-created_at',)  # Default ordering (latest orders first)
    readonly_fields = ('created_at', 'total_price')  # Prevent editing timestamps & total price

    fieldsets = (
        ('Order Details', {'fields': ('user', 'product', 'quantity', 'total_price')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )

admin.site.register(Order, OrderAdmin)
