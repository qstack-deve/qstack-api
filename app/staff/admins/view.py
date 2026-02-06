from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from app.models.staff import Staff
from app.models.jobs import Job
from app.models.portfolio import Portfolio, Category, Tag
from app.models.contact import Contact
from rest_framework.decorators import action
from .serializers import (
    MemberSerializer,
    JobSerializer,
    PortfolioSerializer,
    CategorySerializer,
    TagSerializer,
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
    serializer_class = PortfolioSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]
