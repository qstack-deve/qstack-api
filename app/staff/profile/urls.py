from django.urls import path
from ..views import StaffProfileView
from .view import AvatarUpdateView

urlpatterns = [
    path('', StaffProfileView.as_view(), name='staff-profile'),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
]
