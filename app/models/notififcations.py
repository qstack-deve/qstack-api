from django.db import models
import uuid



class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('new_sticker', 'New Sticker'),
        ('payment_received', 'Payment Received'),
        ('payment_reminder', 'Payment Reminder'),
        ('account_update', 'Account Update'),
        ('news', 'News'),
        ('general', 'General'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    recipient = models.ForeignKey("User", on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPE_CHOICES, default='general')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
