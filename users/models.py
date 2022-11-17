from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

permissions = (
    ('community_leads', 'Community Leads'),
    ('innovation_exec', 'innovation Exec'),
    ('members', 'members'),
    ('patron', 'patron'),
    ('admin', 'admin'),
    
)

class Users(AbstractUser):
    Email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True,null=True)
    last_name = models.CharField(max_length=30, blank=True,null=True)
    phone_number = models.CharField(max_length=30, blank=True,null=True)
    is_exec = models.BooleanField(default=False)
    is_leader = models.BooleanField(default=False)
    is_member = models.BooleanField(default=True)
    is_patron = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Users"
        db_table = 'users'  
    
    def __str__(self):
        return self.Email
    
