from django.db import models
from users.models import User
from products.models import Product

class Order(models.Model):
    """
    Represents an order placed by a user for a specific product.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField(help_text="The number of products ordered")
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, help_text="Auto-calculated total price"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Order creation timestamp")

    def save(self, *args, **kwargs):
        """ Automatically calculates total price before saving """
        if self.product and self.quantity:
            self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"