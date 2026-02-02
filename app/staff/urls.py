from django.urls import path, include
from .auth import urls as auth_urls
from .views import UserDetailsView
from .admins import urls as admin_router
from rest_framework.routers import DefaultRouter
from .profile import urls as profile_urls

router = DefaultRouter()
# router.register(r'profile', StaffProfileViewSet, basename='staff-profile')

urlpatterns = [
    path("auth/", include(auth_urls)),
    path('user/', UserDetailsView.as_view(), name='my-profile'),
    path("profile/", include(profile_urls)),
    path('notifications/', include('app.staff.notifications.urls')),
    path("admin/", include(admin_router)),
    path("members/", include(admin_router))
]
