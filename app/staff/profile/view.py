from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import AvatarUpdateSerializer
from app.models.staff import Staff

class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = AvatarUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return Staff.objects.get(user=self.request.user)
