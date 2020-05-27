"""View module for handling requests about products"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import ProductType


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for products

    Arguments:
        serializers
    """
    class Meta:
        model = ProductType
        url = serializers.HyperlinkedIdentityField(
            view_name='producttype',
            lookup_field='id'
        )
        fields = ('id', 'name')

class ProductTypes(ViewSet):
    def retrieve(self, request, pk=None):
        product_type = ProductType.objects.get(pk=pk)
        serializer = ProductTypeSerializer(product_type, context={'request': request})
        return Response(serializer.data)
    
    def list(self, request):
        product_types = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_types, many=True, context={'request': request})
        return Response(serializer.data)