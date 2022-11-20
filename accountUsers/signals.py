from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserModel

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        pass

@receiver(post_save, sender=UserModel)
def save_profile(sender, instance, **kwargs):
    pass