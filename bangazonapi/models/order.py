from django.db import models
from .customer import Customer
from .payment_type import PaymentType

class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment_type = models.ForeignKey(PaymentType, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(null=True)
