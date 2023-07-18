from datetime import datetime
import decimal
import sys
import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db import transaction

from subscription.models import Invoice,Subscription

class Payment(models.Model):
    
    class PaymentType(models.TextChoices):
        In = "in"
        Out = "out"
        
    class PaymentMethod(models.TextChoices):
        Cash = "Cash"
        Mpesa = "Mpesa"
        PayBill = "PayBill"
        Bank = "Bank"
        
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)  
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False)
    payment_type = models.CharField(max_length=100, choices=PaymentType.choices, null=False, blank=False,help_text="Whether receiving(in) or sending(out)")
    payment_method = models.CharField(max_length=100, choices=PaymentMethod.choices, null=False, blank=False)
    reference = models.CharField(max_length=100, null=True, blank=True, default='')
    description = models.TextField(null=True, blank=True, default='')
    invoice_id = models.ForeignKey('subscription.Invoice', on_delete=models.DO_NOTHING,related_name='payments')  
    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Payment")
        verbose_name_plural = ("Payments")

    def __str__(self):
        return f"{self.payment_method}:{self.payment_type}"

    def get_absolute_url(self):
        return reverse("payment-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        
        is_creating = self._state.adding  # Check if the model instance is being created or updated         
        if is_creating:
            self.update_invoice_and_subscription()
                # print("", file=sys.stderr)            
            
        super().save(*args, **kwargs)
        
    @transaction.atomic   
    def update_invoice_and_subscription(self):        
        # update invoice
        invoice = Invoice.objects.get(pk=self.invoice_id.invoice_no)        
        if invoice:            
            if self.payment_type == self.PaymentType.In:
                invoice.total_paid = decimal.Decimal(invoice.total_paid + self.amount)
                
                # update subscription status
                total_amount_due = decimal.Decimal(invoice.total_amount + invoice.total_tax_amount) - decimal.Decimal(invoice.total_paid)
                if total_amount_due <= 0:
                    invoice.status = Invoice.InvoiceStatus.Paid
                    
                    subscription = Subscription.objects.get(pk=invoice.subscription_id.id)
                    if subscription:
                        subscription.status = Subscription.SubscriptionStatus.Active
                        subscription.activated_at = datetime.now()
                        subscription.save()
                        
                invoice.save()