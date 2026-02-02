from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from app.health_check import HealthCheckView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api/health/', HealthCheckView.as_view(), name='health_check'),
]
