from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from accounts.models import User

from .models import *
from .serializers import *


class SubscriptionViewset(viewsets.ModelViewSet):
    """ "Subscription viewset"""

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["customer_id", "project_id", "subscription_package_id"]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(created_by=user)


class SubscriptionPackageViewset(viewsets.ModelViewSet):
    """ "SubscriptionPackage viewset"""

    serializer_class = SubscriptionPackageSerializer
    queryset = SubscriptionPackage.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "project_id"]

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(created_by=user)
