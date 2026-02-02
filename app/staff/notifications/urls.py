from django.urls import path
from .views import (
    NotificationListView,
    NotificationMarkAsReadView,
    NotificationMarkAllAsReadView
)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<uuid:id>/read/', NotificationMarkAsReadView.as_view(), name='notification-mark-as-read'),
    path('read-all/', NotificationMarkAllAsReadView.as_view(), name='notification-mark-all-as-read'),
]
