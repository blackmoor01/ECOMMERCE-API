from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.

    Attributes:
        phone_number (str): User's phone number (optional).
        address (str): User's physical address (optional).
        role (str): User's role (e.g., 'customer', 'admin'), defaults to 'customer'.
    """

    phone_number = models.CharField(
        max_length=15, blank=True, null=True, help_text="User's phone number (optional)"
    )
    address = models.TextField(blank=True, null=True, help_text="User's physical address (optional)")
    role = models.CharField(
        max_length=20, default='customer', help_text="User's role (e.g., 'customer', 'admin')"
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='Groups to which this user belongs.',
        related_name='custom_user_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions assigned to this user.',
        related_name='custom_user_set',
        related_query_name='user',
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
