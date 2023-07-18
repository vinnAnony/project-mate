from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("admin/", admin.site.urls),
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/accounts/", include("accounts.urls")),
    path("api/projects/", include("project.urls")),
    path("api/customers/", include("customer.urls")),
    path("api/", include("subscription.urls")),
    path("api/", include("payment.urls")),
]

admin.site.site_header = "BizCore MS Admin"
admin.site.site_title = "BizCore Admin Portal"
admin.site.index_title = "Welcome to BizCore MS"

handler404 = 'bizcore.views.page_not_found_view'