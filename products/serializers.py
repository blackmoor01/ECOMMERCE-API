from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    """
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {'help_text': 'Name of the product'},
            'description': {'help_text': 'Detailed product description'},
            'price': {'help_text': 'Product price in USD'},
            'stock': {'help_text': 'Stock count'},
        }
