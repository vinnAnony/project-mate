from rest_framework import serializers
from django.db import transaction

from .models import *

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        
    @transaction.atomic
    def create(self, validated_data):
        payment = validated_data        
        payment = Payment.objects.create(
            amount = payment["amount"],
            payment_type = payment["payment_type"],
            payment_method = payment["payment_method"],
            reference = payment["reference"],
            description = payment["description"],
            invoice_id = payment["invoice_id"],
            processed_by = payment["processed_by"],
        )                        
        
        Payment.update_invoice_and_subscription(payment)
        
        return payment    