import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from bangazonapi.models import Customer, PaymentType
from datetime import datetime


class TestPaymentTypes(TestCase):

    def setUp(self):
        self.username = "TestUser"
        self.password = "Test123"
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.customer = Customer.objects.create(
            user_id=1, phone_number="615-867-5309", address="123 Testing Street")

    def testPostPaymentType(self):

        new_payment_type = {
            "merchant_name": "Test Bank",
            "account_number": "1234567890",
            "expiration_date": "2020-12-31"
        }

        response = self.client.post(
            reverse('paymenttype-list'), new_payment_type, HTTP_AUTHORIZATION='Token ' + str(self.token)
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(PaymentType.objects.count(), 1)
        self.assertEqual(PaymentType.objects.get(
            id=1).id, 1)

    def testGetPaymentType(self):
        new_payment_type = PaymentType.objects.create(
            customer_id=self.customer.id,
            merchant_name="Test Bank",
            account_number="1234567890",
            expiration_date="2020-12-31",
            created_at=datetime.now())

        response = self.client.get(
            reverse('paymenttype-list'), HTTP_AUTHORIZATION='Token ' + str(self.token)
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(
            response.data[0]["customer_id"], new_payment_type.customer_id)

    def testDeletePaymentType(self):
        new_payment_type = PaymentType.objects.create(
            customer_id=self.customer.id, merchant_name="Test Bank", account_number="1234567890", expiration_date="2020-12-31", created_at=datetime.now())

        response = self.client.delete(
            reverse('paymenttype-detail', kwargs={'pk': 1}), HTTP_AUTHORIZATION='Token ' + str(self.token)
        )

        self.assertEqual(response.status_code, 204)

        response = self.client.get(
            reverse('paymenttype-list'), HTTP_AUTHORIZATION='Token ' + str(self.token)
        )

        self.assertEqual(len(response.data), 0)


if __name__ == "__main__":
    unittest.main()
