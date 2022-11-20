from django.db import models
from  django.contrib.auth.models  import  AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    email=models.EmailField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100)
    is_excutive=models.BooleanField(default=False)
    is_lead=models.BooleanField(default=False)
    is_member=models.BooleanField(default=True)
    is_patron=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Users"
        db_table = 'user'
        
    def __str__(self):
        return self.email
    