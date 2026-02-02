from app.models import (
    Notification,
    User,
)

def create_notification(recipient: User, title: str, message: str, notification_type: str = 'general'):
    """
    Creates a notification for a user.
    """
    notification = Notification.objects.create(
        recipient=recipient,
        title=title,
        message=message,
        notification_type=notification_type
    )
    return notification