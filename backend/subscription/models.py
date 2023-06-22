import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class SubscriptionPackage(models.Model):
    class SubscriptionDuration(models.TextChoices):
        Day = 'Day'
        Week = 'Week'
        Month = 'Month'
        Year = 'Year'
        OneTime = 'One-Time'
        
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    name = models.CharField(max_length=255,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2,null=False,blank=False)
    duration = models.CharField(max_length=100, choices=SubscriptionDuration.choices,null=False,blank=False)
    project_id = models.ForeignKey("project.Project", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Subscription Package")
        verbose_name_plural = ("Subscription Packages")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subscription-package-detail", kwargs={"pk": self.pk})


class Subscription(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    customer_id = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    project_id = models.ForeignKey("project.Project", on_delete=models.CASCADE)
    subscription_package_id = models.ForeignKey(SubscriptionPackage , on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Subscription")
        verbose_name_plural = ("Subscriptions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subscription-detail", kwargs={"pk": self.pk})
