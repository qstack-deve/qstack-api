from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import StaffViewSet, JobViewSet, PortfolioViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'portfolio', PortfolioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
