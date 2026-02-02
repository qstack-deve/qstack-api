
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.users import User
from .models.staff import Staff

@receiver(post_save, sender=User)
def create_staff_profile(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(user=instance)
