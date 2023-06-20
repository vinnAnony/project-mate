from django.urls import path, include

from accounts import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'register', views.RegisterUserViewSet,basename='register')
router.register(r'users', views.UserViewSet,basename='user')

urlpatterns = [
    # path('forgot-password/', views.ForgotPasswordView.as_view()),
    # logout/ [name='logout']
    # forgot-password/ [name='forgot_password']
    # password-reset/ [name='password_reset']
    # reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # forgot-password/done/ [name='forgot_password_done']=>front-end
    # password-reset/done/ [name='password_reset_done']=>front-end
    # reset/done/ [name='password_reset_complete']=>front-end
]

urlpatterns += router.urls