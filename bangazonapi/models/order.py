from django.db import models
from .customer import Customer
from .payment_type import PaymentType

class Order(models.Model):

    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField()