from django.urls import path, include

from accounts import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'register', views.RegisterUserViewSet,basename='register')
router.register(r'users', views.UserViewSet,basename='user')

urlpatterns = [
    # path('forgot-password/', views.ForgotPasswordView.as_view()),
]

urlpatterns += router.urls