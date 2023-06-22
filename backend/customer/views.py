from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from accounts.models import User

from .models import *
from .serializers import *

class CustomerViewset(viewsets.ModelViewSet):
    """"customer viewset"""
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phone_number','email','location']

    def perform_create(self, serializer):
        # set logged in user to project created before saving
        user = User.objects.get(id=self.request.user.id)
        serializer.save(created_by=user)