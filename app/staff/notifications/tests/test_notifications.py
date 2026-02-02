from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.models.users import User
from apps.notifications.models import Notification
from apps.notifications.services import create_notification

class NotificationAPITests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(email='user1@example.com', password='password123', role='taxpayer')
        self.user2 = User.objects.create_user(email='user2@example.com', password='password123', role='taxpayer')
        self.client.force_authenticate(user=self.user1)

        self.notification1 = create_notification(
            recipient=self.user1,
            title='Test Notification 1',
            message='This is a test notification for user 1.',
            notification_type='general'
        )
        self.notification2 = create_notification(
            recipient=self.user1,
            title='Test Notification 2',
            message='This is another test notification for user 1.',
            notification_type='account_update'
        )
        self.notification3 = create_notification(
            recipient=self.user2,
            title='Test Notification 3',
            message='This is a test notification for user 2.',
            notification_type='general'
        )

    def test_list_notifications(self):
        """
        Ensure a user can only list their own notifications.
        """
        url = reverse('notification-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.notification2.title)
        self.assertEqual(response.data[1]['title'], self.notification1.title)

    def test_mark_notification_as_read(self):
        """
        Ensure a user can mark their own notification as read.
        """
        self.assertFalse(self.notification1.read)
        url = reverse('notification-mark-as-read', kwargs={'id': self.notification1.id})
        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.notification1.refresh_from_db()
        self.assertTrue(self.notification1.read)

    def test_cannot_mark_other_user_notification_as_read(self):
        """
        Ensure a user cannot mark another user's notification as read.
        """
        url = reverse('notification-mark-as-read', kwargs={'id': self.notification3.id})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mark_all_notifications_as_read(self):
        """
        Ensure a user can mark all their notifications as read.
        """
        self.assertTrue(Notification.objects.filter(recipient=self.user1, read=False).exists())

        url = reverse('notification-mark-all-as-read')
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Notification.objects.filter(recipient=self.user1, read=False).exists())

    def test_create_notification_service(self):
        """
        Test the notification creation service.
        """
        notification = create_notification(
            recipient=self.user1,
            title='Service Test',
            message='Testing the service.',
            notification_type='news'
        )
        self.assertIsInstance(notification, Notification)
        self.assertEqual(notification.recipient, self.user1)
        self.assertEqual(notification.title, 'Service Test')
        self.assertEqual(notification.notification_type, 'news')
