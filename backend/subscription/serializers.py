from rest_framework import serializers
from django.db import transaction

from .models import *


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
        
        @transaction.atomic
        def create(self, validated_data):
            subscription = validated_data
            invoice = dict(validated_data['invoice'])

            
            subscription = Subscription.objects.create(
                customer_id = subscription["customer_id"],
                project_id = subscription["project_id"],
                subscription_package_id = subscription["subscription_package_id"],
                created_by = subscription["created_by"],
            )
            
            try:                
                invoice = Invoice.objects.create(
                    subscription_id = subscription.id,
                    total_amount = subscription.subscription_package_id.price,
                    tax_percentage = invoice["tax_percentage"],
                    total_tax_amount = (invoice["tax_percentage"] * subscription.subscription_package_id.price)/100,
                    due_date = invoice["due_date"],
                ).save()
                
            except Exception as ex:
                return ex

            return subscription


class SubscriptionPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPackage
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"