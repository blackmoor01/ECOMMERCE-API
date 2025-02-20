from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import User
from .serializers import UserSerializer

@extend_schema_view(
    list=extend_schema(
        summary="List all users",
        description="Retrieve a list of registered users. Requires authentication.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a user",
        description="Fetch details of a specific user by ID.",
    ),
    create=extend_schema(
        summary="Register a new user",
        description="Allows public access for user registration. Requires username, email, and password.",
    ),
    update=extend_schema(
        summary="Update a user",
        description="Update an existing user's information. Requires authentication.",
    ),
    partial_update=extend_schema(
        summary="Partially update a user",
        description="Partially update specific fields of a user.",
    ),
    destroy=extend_schema(
        summary="Delete a user",
        description="Delete a user permanently. Requires admin privileges.",
    ),
)
class UserViewSet(viewsets.ModelViewSet):
    """
    User API endpoint to perform CRUD operations on users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Grants public access for user registration but requires authentication for other actions.
        """
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
