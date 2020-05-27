from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazonapi.models import Product, Customer, ProductType
from datetime import datetime


class SellSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for Selling Products
    Arguments:
        serializers
    """
    class Meta:
        model = Product
        url = serializers.HyperlinkedIdentityField(
            view_name='product',
            lookup_field='id'
        )
        fields = ('id', 'title', 'price', 'description', 'quantity', 'location', 'image_path', 'product_type_id')
        depth = 1

class Sell(ViewSet):
    def create(self, request):
        newproduct = Product()
        # product type refers to a foreign key
        product_type = ProductType.objects.get(pk=request.data["product_type"])
        # customer refers to the user
        customer = Customer.objects.get(user=request.auth.user)
        # request all other data
        newproduct.title = request.data["title"] 
        newproduct.price = request.data["price"] 
        newproduct.description = request.data["description"] 
        newproduct.quantity = request.data["quantity"] 
        newproduct.location = request.data["location"] 
        newproduct.image_path = request.data["image_path"]
        # May be handling created at on the front end using Date.now()
        newproduct.created_at = request.data["created_at"]
        newproduct.customer = customer
        newproduct.product_type = product_type
        newproduct.created_at = datetime.now()

        newproduct.save()

        serializer = SellSerializer(
            newproduct, context={'request': request}
        )

        return Response(serializer.data)
    # Will list all products that can be sold
    def list(self, request): 
        sell_products = Product.objects.all()
        serializer = SellSerializer(
            sell_products, 
            many=True, 
            context={'request': request}
        )
        return Response(serializer.data)
    # Will retrieve a specific sellable product
    def retrieve(self, request, pk=None): 
        try: 
            sell_product = Product.objects.get(pk=pk)
            serializer = SellSerializer(
                sell_product, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex: 
            return HttpResponseServerError(ex)
