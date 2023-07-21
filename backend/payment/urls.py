from django.urls import path, include

from rest_framework_nested import routers
from .views import *

router = routers.SimpleRouter()

router.register(r"payments", PaymentViewset, basename="payment")


urlpatterns = [
    path(r'', include(router.urls)),
    path('pay/stk-push', stk_push),
]