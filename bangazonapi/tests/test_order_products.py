import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from bangazonapi.models import Customer, Order, OrderProduct, Product, ProductType
from datetime import datetime


class TestOrderProducts(TestCase):

    def setUp(self):
        self.username = 'TestUser'
        self.password = 'Test123'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.customer = Customer.objects.create(user_id=1, phone_number="615-356-3467", address="123 Testing Street")
        self.order = Order.objects.create(created_at="2020-06-03 18:48:48.621102", customer_id=1, payment_type_id=None)
        self.product = Product.objects.create(title="test item", price=200, description="test description", quantity=1, location="test", image_path="test.png", created_at="2020-06-03 18:48:48.621102", customer_id=1, product_type_id=1)
        self.product_type = ProductType.objects.create(name="test category")

    def testPostOrderProduct(self):

        new_order_product = {
            "order_id": 1,
            "product_id": 1
        }

        response = self.client.post(
            reverse('orderproduct-list'), new_order_product, HTTP_AUTHORIZATION='Token ' + str(self.token))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(OrderProduct.objects.count(), 1)

        self.assertEqual(OrderProduct.objects.get(id=1).order_id, new_order_product["order_id"])

    def testGetOrder(self):
        new_order_product = OrderProduct.objects.create(
            order_id=1,
            product_id=1
        )
        
        response = self.client.get(
            reverse('orderproduct-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["order_id"], new_order_product.order_id)

    def testDeleteOrder(self):
        new_order_product = OrderProduct.objects.create(
            order_id=1,
            product_id=1
        )

        response = self.client.delete(
            reverse('orderproduct-detail', kwargs={'pk': 1}), HTTP_AUTHORIZATION='Token ' + str(self.token))

        self.assertEqual(response.status_code, 204)

        response = self.client.get(
            reverse('orderproduct-list'), HTTP_AUTHORIZATION='Token ' + str(self.token))
        self.assertEqual(len(response.data), 0)


if __name__ == '__main__':
    unittest.main()