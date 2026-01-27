from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
import uuid


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField("app.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="profile")
    
    full_name = models.CharField(max_length=100) 
    phone = models.CharField(max_length=20)     
    address = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone})"
