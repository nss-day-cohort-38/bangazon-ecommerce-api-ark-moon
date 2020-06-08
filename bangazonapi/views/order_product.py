"""View module for handling requests about order products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import OrderProduct, Order, Product

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrderProduct
        url = serializers.HyperlinkedIdentityField(
            view_name='orderproduct',
            lookup_field='id'
        )
        fields = ('id', 'order_id', 'product_id', 'product')
        depth = 2


class OrderProducts(ViewSet):
    def list(self, request):

        order_products = OrderProduct.objects.all()

        order_id = self.request.query_params.get('order_id', None)

        if order_id is not None:
            order_products = order_products.filter(order_id = order_id)
        serializer = OrderProductSerializer(order_products, many=True, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            order_product = OrderProduct.objects.get(pk=pk)
            serializer = OrderProductSerializer(order_product, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        new_order_product = OrderProduct()

        product = Product.objects.get(pk=request.data['product_id'])
        order = Order.objects.get(pk=request.data['order_id'])

        new_order_product.product = product
        new_order_product.order = order

        new_order_product.save()

        serializer = OrderProductSerializer(new_order_product, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        
        try:
            order_product = OrderProduct.objects.get(pk=pk)
            order_product.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except OrderProduct.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)