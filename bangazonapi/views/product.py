"""View module for handling requests about products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Product,Customer


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for products

    Arguments:
        serializers
    """
    # product_type = ProductTypeSerializer()

    class Meta:
        model = Product
        url = serializers.HyperlinkedIdentityField(
            view_name='product',
            lookup_field='id'
        )
        fields = ('id', 'title', 'price', 'description', 'quantity', 'location', 'image_path', 'customer_id', 'product_type_id', 'created_at', 'product_type')
        depth = 1

class Products(ViewSet):

    def list(self, request):
        products = Product.objects.all()
        # product_type = self.request.query_params.get('product_type', None)
        # if product_type is not None:
        #     products = products.filter(product_id=product_type)

        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    # Handle POST operations
    def create(self, request):
        new_product = Product()
        new_product.name = request.data["title"]
        new_product.customer = request.data["customer"]
        new_product.description = request.data["description"]
        new_product.quantity = request.data["quantity"]
        new_product.location = request.data["location"]
        new_product.image_path = request.data["image_path"]
        new_product.created_at = request.data["created_at"]
        new_product.product_type = request.data["product_type"]


        product = Product.objects.get(pk=request.data["product_type"])
        print("PRODUCT", product)
        new_product.product_type = product
        print("NEW_PRODUCT", new_product)
        new_product.save()

        serializer = ProductSerializer(new_product, context={'request': request})
        return Response(serializer.data)

    # Handle PUT requests for a park area attraction
    def update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        customer = Customer.objects.get(pk=request.data["customer"])

        product.name = request.data["title"]
        product.customer = request.data["customer"]
        product.description = request.data["description"]
        product.quantity = request.data["quantity"]
        product.location = request.data["location"]
        product.image_path = request.data["image_path"]
        product.created_at = request.data["created_at"]
        product.product_type = request.data["product_type"]

        product.customer = customer
        product.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single park are
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Product.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
