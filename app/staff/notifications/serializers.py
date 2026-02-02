from rest_framework import serializers
from app.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'recipient', 'title', 'message', 'read', 'notification_type', 'created_at')
        read_only_fields = ('id', 'created_at', 'recipient')
