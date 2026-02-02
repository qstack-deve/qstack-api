from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
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
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # Only authenticated staff/admins should see the role list
    permission_classes = [IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    # Only authenticated staff/admins should see the skill list
    permission_classes = [IsAuthenticated]

class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialsSerializer
    # Only authenticated staff/admins should see the social list
    permission_classes = [IsAuthenticated]