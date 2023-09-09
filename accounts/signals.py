from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import CustomUser, Profile

@receiver(post_save, sender=CustomUser)
def create_profile_signal(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)