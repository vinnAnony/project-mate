from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle

from .models import *
from .serializers import * 
from .throttles import AccountsRateThrottle


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """Api View for listing all users and retrieving specific users using their id's"""

    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle, AccountsRateThrottle]
    
    def get_queryset(self):        
        return User.objects.all()

class RegisterUserViewSet(CreateModelMixin, GenericViewSet):
    """Api view to be used when a user first registers to the system"""

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    throttle_classes = [UserRateThrottle, AccountsRateThrottle]
