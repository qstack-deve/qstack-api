from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from rest_framework.response import Response
from app.models.staff import Staff, Role, Skill, Social
from app.models.users import User
from .serializers import (
    SkillSerializer,
    RoleSerializer,
    SocialsSerializer,
    UserSerializer, StaffProfileSerializer
)
class UserDetailsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class StaffProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StaffProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return Staff.objects.get(user=user)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.annotate(staff_count=Count('staff')).order_by('-level')
    serializer_class = RoleSerializer

    permission_classes = [IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialsSerializer
    permission_classes = [IsAuthenticated]