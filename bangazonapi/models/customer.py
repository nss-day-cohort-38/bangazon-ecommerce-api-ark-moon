from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=55)
    address = models.CharField(max_length=255)

    class Meta:
        ordering = (F('id').asc(nulls_last=True),)