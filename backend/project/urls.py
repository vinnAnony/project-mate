from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.ProjectViewset,basename='project')

urlpatterns = [
    # path('forgot-password/', views.ForgotPasswordView.as_view()),
]

urlpatterns += router.urls