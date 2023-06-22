from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.authentication import (SessionAuthentication,TokenAuthentication)
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from .models import *
from .serializers import *
from .throttles import *
from .filters import *

"""List and create projects using ListCreateAPIView"""
# class ProjectList(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     throttle_classes = [UserRateThrottle, ProjectRateThrottle]
#     filter_backends = (DjangoFilterBackend,)   
#     filterset_class = ProjectFilter
    
    
class ProjectViewset(viewsets.ModelViewSet):
    """"project viewset"""
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        # set logged in user to project created before saving
        user = User.objects.get(id=self.request.user.id)
        serializer.save(created_by=user)