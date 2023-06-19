from django.urls import path, include

from accounts import views

urlpatterns = [
    path('auth/register/', views.RegisterAccountViewSet.as_view({'post:create'}),name='register'),
    path('users/', views.UserViewSet.as_view({'get':'list'}),name='users'),
]