from django.db import models
from .customer import Customer
from .product_type import ProductType

class Product(models.Model):

    title = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    location = models.CharField(max_length=75)
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title

