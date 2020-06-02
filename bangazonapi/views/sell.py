from django.http import HttpResponse, HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazonapi.models import Product, Customer, ProductType
from datetime import datetime
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView


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
        fields = ('id', 'title', 'price', 'description', 'quantity', 'location', 'image_path', 'product_type')
        depth = 1
       

class Sell(ViewSet):
    parser_class = (FileUploadParser,)
    def create(self, request):
        print(request.data)
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

# class FileSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Product
#         # Do we need a URL?
#         # url = serializers.HyperlinkedIdentityField(
#         #     view_name='media',
#         #     lookup_field='id'
#         # )
#         fields = "image_path"

# class FileUploadView(APIView):
#     parser_class = (FileUploadParser,)

    # def post(self, request, *args, **kwargs):
    # #The request.data property will be a dictionary with a single key file containing the uploaded file.
    #   file_serializer = FileSerializer(data=request.data)

    #   if file_serializer.is_valid():
    #       file_serializer.save()
    #       return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #   else:
    #       return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)