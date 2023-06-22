from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r"subscriptions", views.SubscriptionViewset, basename="subscription")
router.register(
    r"subscription-packages", views.SubscriptionViewset, basename="subscription-package"
)

urlpatterns = []

urlpatterns += router.urls
