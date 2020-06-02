"""View module for handling requests about products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Product, Customer, Order, PaymentType
from django.contrib.auth.models import User


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

        # changing this from Order.objects.all() to only pull the orders for the logged in user
        orders = Order.objects.get(user=request.auth.user)

        serializer = OrdertSerializer(orders, many=True, context={'request': request})
        return Response(serializer.data)


    def create(self, request):
        new_order = Order()

        customer = Customer.objects.get(user=request.auth.user)
        product = Product.objects.get(pk=request.data["product_type"])

        user = User.objects.get(pk=request.data["customer_id"])
        customer = Customer.objects.get(user=user)
        payment_type = PaymentType.objects.get(user=customer)
        orders = Order.objects.filter(customer=customer)

        new_order.customer = customer
        new_order.payment_type = payment_type
        new_order.created_at = request.data["created_at"]


        print("NEW_PRODUCT", new_order)
        new_order.save()

        serializer = OrdertSerializer(new_order, context={'request': request})
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
