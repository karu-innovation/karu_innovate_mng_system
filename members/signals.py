from django.db.models.signals import post_save
from django.dispatch import receiver
from accountUsers.models import UserModel
from .models import Members

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserModel.objects.create(user=instance, 
                                email=instance.email, 
                                first_name=instance.first_name, 
                                last_name=instance.last_name, 
                                phone_number=instance.phone_number,
                                password=instance.reg_no)




@receiver(post_save, sender=UserModel)
def save_profile(sender, instance, **kwargs):
    instance.user.save()