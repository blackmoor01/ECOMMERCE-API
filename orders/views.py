from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from .models import Order
from .serializers import OrderSerializer

@extend_schema_view(
    list=extend_schema(
        summary="Retrieve a list of orders",
        description="Returns a paginated list of all orders placed by users.",
        parameters=[
            OpenApiParameter(name="user", description="Filter by user ID", required=False, type=int),
            OpenApiParameter(name="product", description="Filter by product ID", required=False, type=int),
            OpenApiParameter(name="ordering", description="Order by created_at or total_price", required=False, type=str),
        ],
    ),
    retrieve=extend_schema(
        summary="Retrieve a specific order",
        description="Fetches the details of a single order based on the provided order ID.",
    ),
    create=extend_schema(
        summary="Create a new order",
        description="Allows an authenticated user to create a new order.",
    ),
    update=extend_schema(
        summary="Update an order",
        description="Modifies an existing order. Only available for specific use cases.",
    ),
    partial_update=extend_schema(
        summary="Partially update an order",
        description="Allows updating specific fields of an existing order.",
    ),
    destroy=extend_schema(
        summary="Delete an order",
        description="Deletes an order permanently. Only admins or the owner can perform this action.",
    ),
)
class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create, retrieve, update, and delete orders.
    """

    queryset = Order.objects.select_related('user', 'product').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'product']
    ordering_fields = ['created_at', 'total_price']
    ordering = ['-created_at']
