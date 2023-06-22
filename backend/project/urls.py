from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'', views.ProjectViewset,basename='project')

urlpatterns = [
    
]

urlpatterns += router.urls