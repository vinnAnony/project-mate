from rest_framework import serializers
from django.db import transaction
from django.forms.models import model_to_dict

from .models import *
from mail.email import send_email
from .tasks import generate_and_email_invoice_pdf

from datetime import datetime, timedelta
import logging
logger = logging.getLogger(__name__)
 # logger.warning("log")
 
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
        
    @transaction.atomic
    def create(self, validated_data):
        subscription = validated_data        
        subscription = Subscription.objects.create(
            customer_id = subscription["customer_id"],
            project_id = subscription["project_id"],
            subscription_package_id = subscription["subscription_package_id"],
            created_by = subscription["created_by"],
        )
        
        invoice = Invoice.objects.create(
                subscription_id = subscription,
                total_amount = subscription.subscription_package_id.price,
                # TODO: - set default tax % in system config
                tax_percentage = 16,
                # TODO: - set default due_date in system config
                due_date = datetime.now() + timedelta(days=14),
                generated_by = subscription.created_by,
            )
        
        # send new subscription email
        send_email(
            context={
                'customer': subscription.customer_id.name,
                'project': model_to_dict(subscription.subscription_package_id.project_id),
                'subscription': model_to_dict(subscription.subscription_package_id),
                'company':{
                    'name':'ProjectMate'
                }
                },
            template='new_subscription',
            recipients=[subscription.customer_id.email]
        )
        
        # generate and email invoice pdf
        generate_and_email_invoice_pdf.delay(invoice.pk)

        return subscription


class SubscriptionPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPackage
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"