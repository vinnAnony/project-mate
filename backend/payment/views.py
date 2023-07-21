from django.conf import settings
from django.db import transaction
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from mpesa.daraja.core import MpesaClient

from .models import Payment
from .serializers import *

class PaymentViewset(viewsets.ModelViewSet):
    """ "Payment viewset"""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["reference", "payment_method", "created_at"]
    
@api_view(["POST"])
def stk_push(request):
    cl = MpesaClient()
    
    serializer = StkPushSerializer(data=request.data)

    if serializer.is_valid():    
        phone_number = serializer.validated_data['phone_number']
        amount = serializer.validated_data['amount']
        account_reference = serializer.validated_data['account_reference']
        transaction_desc = 'Payment'
        callback_url = settings.MPESA_EXPRESS_CALLBACK_URL
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        
        return Response(response)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)