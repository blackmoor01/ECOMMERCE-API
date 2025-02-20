from django.db import models

class Product(models.Model):
    """
    Represents a product in the e-commerce platform.
    """
    name = models.CharField(
        max_length=255,
        help_text="Name of the product."
    )
    description = models.TextField(
        help_text="Detailed description of the product."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price of the product in USD."
    )
    stock = models.IntegerField(
        help_text="Number of items available in stock."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the product was added."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the product was last updated."
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return self.name