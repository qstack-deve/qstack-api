from rest_framework import viewsets, generics
from app.models.staff import Staff
from app.models.jobs import Job
from app.models.portfolio import Portfolio
from app.models.contact import Contact
from .serializers import (
    StaffSerializer,
    JobSerializer,
    PortfolioListSerializer,
    ContactSerializer
)


class StaffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    lookup_field = 'slug'
    serializer_class = StaffSerializer


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioListSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
