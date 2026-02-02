from rest_framework import serializers
from app.models.staff import Staff

class AvatarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('avatar',)
