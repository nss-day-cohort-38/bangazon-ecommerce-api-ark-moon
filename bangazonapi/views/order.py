"""View module for handling requests about products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Customer, Order, PaymentType
from datetime import datetime


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        url = serializers.HyperlinkedIdentityField(
            view_name='order',
            lookup_field='id'
        )
        fields = ('id', 'customer', 'customer_id', 'payment_type', 'created_at', )
        depth = 1


class Orders(ViewSet):
    def list(self, request):

        # getting the logged in user
        customer = Customer.objects.get(user=request.auth.user)

        # only pulling the orders for the logged in user
        orders = Order.objects.filter(customer=customer)

        serializer = OrderSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        new_order = Order()

        customer = Customer.objects.get(user=request.auth.user)
        new_order.customer = customer

        new_order.payment_type = None
        new_order.created_at = datetime.now()

        new_order.save()

        serializer = OrderSerializer(new_order, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        order = Order.objects.get(pk=pk)

        payment_type = PaymentType.objects.get(pk=request.data["payment_type_id"])
        order.payment_type = payment_type

        order.save()

    def destroy(self, request, pk=None):
        
        try:
            order = Order.objects.get(pk=pk)
            order.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
