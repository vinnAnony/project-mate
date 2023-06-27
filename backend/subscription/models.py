import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class SubscriptionPackage(models.Model):
    class SubscriptionDuration(models.TextChoices):
        Day = "Day"
        Week = "Week"
        Month = "Month"
        Year = "Year"
        OneTime = "One-Time"

    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(
        max_digits=11, decimal_places=2, null=False, blank=False
    )
    duration = models.CharField(
        max_length=100, choices=SubscriptionDuration.choices, null=False, blank=False
    )
    project_id = models.ForeignKey("project.Project", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False
    )

    class Meta:
        verbose_name = "Subscription Package"
        verbose_name_plural = "Subscription Packages"

    def __str__(self):
        return f"{self.project_id} - {self.name}"

    def get_absolute_url(self):
        return reverse("subscription-package-detail", kwargs={"pk": self.pk})


class Subscription(models.Model):
    class SubscriptionStatus(models.TextChoices):
        PendingPayment = "Pending Payment"
        Active = "Active"
        Suspended = "Suspended"
        Cancelled = "Cancelled"
        
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    customer_id = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    project_id = models.ForeignKey("project.Project", on_delete=models.CASCADE)
    subscription_package_id = models.ForeignKey(
        SubscriptionPackage, on_delete=models.CASCADE
    )
    status = models.CharField(max_length=100, choices=SubscriptionStatus.choices, null=False, blank=False,default=SubscriptionStatus.PendingPayment)
    activated_at = models.DateTimeField(null=True, blank=True)
    suspended_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False
    )

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return f"{self.subscription_package_id}: {self.customer_id}"

    def get_absolute_url(self):
        return reverse("subscription-detail", kwargs={"pk": self.pk})

# TODO: -create invoice on subscription creation