from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializes the Order model for API interactions.
    """

    user = serializers.StringRelatedField(help_text="Username of the order owner")
    product = serializers.StringRelatedField(help_text="Name of the ordered product")
    quantity = serializers.IntegerField(help_text="Number of items ordered")
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
        help_text="Total price automatically calculated as quantity * product price"
    )
    created_at = serializers.DateTimeField(read_only=True, help_text="Timestamp when the order was placed")

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total_price', 'created_at']
