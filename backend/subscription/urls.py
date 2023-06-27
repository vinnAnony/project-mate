from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r"subscriptions", views.SubscriptionViewset, basename="subscription")
router.register(r"subscription-packages", views.SubscriptionPackageViewset, basename="subscription-package")
router.register(r"invoices", views.InvoiceViewset, basename="invoice")

urlpatterns = []

urlpatterns += router.urls
