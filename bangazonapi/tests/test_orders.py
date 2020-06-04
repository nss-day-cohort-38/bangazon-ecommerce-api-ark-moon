import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from bangazonapi.models import Customer, Order
from datetime import datetime


class TestOrders(TestCase):

    def setUp(self):
        self.username = 'TestUser'
        self.password = 'Test123'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.customer = Customer.objects.create(user_id=1, phone_number="615-356-3467", address="123 Testing Street")

    def testPostOrder(self):

        new_order = {}

        response = self.client.post(
            reverse('order-list'), new_order, HTTP_AUTHORIZATION='Token ' + str(self.token))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(Order.objects.count(), 1)

        self.assertEqual(Order.objects.get(id=1).payment_type_id, None)

    def testGetOrder(self):
        new_order = Order.objects.create(
            customer_id=1,
            payment_type_id=None,
            created_at=datetime.now()
        )
        
        response = self.client.get(
            reverse('order-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["customer_id"], new_order.customer_id)

    def testDeleteOrder(self):
        new_order = Order.objects.create(
            customer_id=1,
            payment_type_id=None,
            created_at=datetime.now()
        )

        response = self.client.delete(
            reverse('order-detail', kwargs={'pk': 1}), HTTP_AUTHORIZATION='Token ' + str(self.token))

        self.assertEqual(response.status_code, 204)

        response = self.client.get(
            reverse('order-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))
        self.assertEqual(len(response.data), 0)

if __name__ == '__main__':
    unittest.main()




