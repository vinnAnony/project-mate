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
        
        return payment    
    
class StkPushSerializer(serializers.Serializer):        
    phone_number = serializers.CharField(max_length=100)
    amount = serializers.IntegerField(min_value=1,max_value=300000)
    account_reference = serializers.CharField(max_length=100)       