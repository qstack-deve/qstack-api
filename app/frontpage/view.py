from rest_framework import viewsets
from app.models.staff import Staff
from app.models.jobs import Job
from app.models.portfolio import Portfolio
from .serializers import (
    StaffListSerializer,
    StaffDetailSerializer,
    JobSerializer,
    PortfolioListSerializer,
)


class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return StaffListSerializer
        return StaffDetailSerializer


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioListSerializer
