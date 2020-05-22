from django.db import models
from .product import Product
from .order import Order

class OrderProduct(models.Model):

    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)