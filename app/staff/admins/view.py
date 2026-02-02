from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from app.models.staff import Staff
from app.models.jobs import Job
from app.models.portfolio import Portfolio
from app.models.contact import Contact
from rest_framework.decorators import action
from .serializers import (
    MemberSerializer,
    JobSerializer,
    PortfolioListSerializer,
)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'

    # def get_serializer_class(self):
    #     if self.request.method in ['POST', 'PUT', 'PATCH']:
    #         return MemberWriteSerializer
    #     return MemberSerializer

    # 1. Custom Action: Activate
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def activate(self, request, id=None):
        member = self.get_object()
        member.active_status = 'active'
        member.save()
        return Response({'status': 'Member activated'}, status=status.HTTP_200_OK)

    # 2. Custom Action: Suspend
    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def suspend(self, request, id=None):
        member = self.get_object()
        member.active_status = 'suspended'
        member.save()
        return Response({'status': 'Member suspended'}, status=status.HTTP_200_OK)
        

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioListSerializer
