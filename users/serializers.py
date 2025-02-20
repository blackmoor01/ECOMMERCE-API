from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    Handles secure password hashing during user creation.
    """

    password = serializers.CharField(
        write_only=True, required=True, help_text="Password for the user (write-only)"
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address', 'role', 'password']
        read_only_fields = ['id']
        extra_kwargs = {
            'username': {'help_text': 'Unique username for the user'},
            'email': {'help_text': 'Email address of the user'},
            'phone_number': {'help_text': "User's phone number"},
            'address': {'help_text': "User's physical address"},
            'role': {'help_text': "Role of the user ('customer', 'admin')"},
        }

    def create(self, validated_data):
        """
        Overriding the create method to securely hash the user's password.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
