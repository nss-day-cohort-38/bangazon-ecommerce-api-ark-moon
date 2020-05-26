from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazonapi.models import PaymentType, Customer
from datetime import datetime

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        url = serializers.HyperlinkedIdentityField(
            view_name='paymenttype',
            lookup_field='id'
        )
        fields = ('id', 'url','merchant_name', 'account_number', 'expiration_date', 'created_at', 'customer_id')

class PaymentTypes(ViewSet):

    def create(self, request):

        new_payment_type = PaymentType()
        new_payment_type.merchant_name = request.data["merchant_name"]
        new_payment_type.account_number = request.data["account_number"]
        new_payment_type.expiration_date = request.data["expiration_date"]
        new_payment_type.created_at = datetime.now()

        customer = Customer.objects.get(user=request.auth.user)
        new_payment_type.customer = customer

        new_payment_type.save()

        serializer = PaymentTypeSerializer(new_payment_type, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            payment_type = PaymentType.objects.get(pk=pk)
            serializer = PaymentTypeSerializer(
                payment_type, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
       