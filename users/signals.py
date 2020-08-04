from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from .models import Profile


@receiver(post_save, sender=get_user_model())
def create_related_profile(sender, instance, created, **kwargs):
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)
