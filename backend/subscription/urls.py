from django.urls import path, include

from rest_framework_nested import routers
from .views import *

router = routers.SimpleRouter()

router.register(r"subscription-packages", SubscriptionPackageViewset, basename="subscription-package")
router.register(r"subscriptions", SubscriptionViewset, basename="subscription")
router.register(r"invoices", InvoiceViewset, basename="invoice")

# /subscription-packages/{id}/subscriptions/
subscription_package_router = routers.NestedSimpleRouter(router, r'subscription-packages', lookup='subscription_package')
subscription_package_router.register(r"subscriptions", SubscriptionViewset, basename="subscription-package-subscriptions")

# /subscriptions/{id}/invoices/
subscription_router = routers.NestedSimpleRouter(router, r'subscriptions', lookup='subscription')
subscription_router.register(r"invoices", InvoiceViewset, basename="subscription-invoices")


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(subscription_package_router.urls)),
    path(r'', include(subscription_router.urls))
]

