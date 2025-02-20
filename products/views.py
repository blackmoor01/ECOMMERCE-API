from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import Product
from .serializers import ProductSerializer

@extend_schema_view(
    list=extend_schema(summary="Retrieve a list of products"),
    retrieve=extend_schema(summary="Get details of a specific product"),
    create=extend_schema(summary="Create a new product"),
    update=extend_schema(summary="Update an existing product"),
    partial_update=extend_schema(summary="Partially update a product"),
    destroy=extend_schema(summary="Delete a product"),
)
class ProductViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for the Product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']