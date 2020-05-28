from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazonapi.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(
            view_name='customer',
            lookup_field='id'
        )
        fields = ('id', 'url', 'address', 'phone_number', 'user_id', 'user')
        depth = 1


class Customers(ViewSet):

    def retrieve(self, request, pk=None):

        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(
                customer, context={
                    'request': request
                }
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        customers = Customer.objects.all()
        serializer = CustomerSerializer(
            customers,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)