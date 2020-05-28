"""View module for handling requests about products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Product, Customer, Order

class OrdertSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        url = serializers.HyperlinkedIdentityField(
            view_name='orders',
            lookup_field='id'
        )
        fields = ('id', 'customer', 'payment_type', 'created_at', )
        depth = 1

class Orders(ViewSet):
        def list(self, request):

            customer = Customer.objects.get(user=request.customer.user)
            print("customer", customer)

            orders = Order.objects.filter(customer=customer)
            serializer = OrdertSerializer(orders, many=True, context={'request': request})
            return Response(serializer.data)
