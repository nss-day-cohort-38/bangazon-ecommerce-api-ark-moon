from django.db import models
from .customer import Customer

class PaymentType(models.Model):

    merchant_name = models.CharField(max_length=25)
    account_number = models.CharField(max_length=25)
    expiration_date = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField()