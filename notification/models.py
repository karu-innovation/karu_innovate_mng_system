from django.db import models
from accountUsers.models import UserModel
# Create your models here.
class Notification(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    sender=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='sender')
    message=models.CharField(max_length=100,blank=False,null=False)
    timestap=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Notification'
        db_table='notification'
        
    def __str__(self):
        return self.name