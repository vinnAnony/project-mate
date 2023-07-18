from django.db import transaction
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)

from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewset(viewsets.ModelViewSet):
    """ "Payment viewset"""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["reference", "payment_method", "created_at"]
    
