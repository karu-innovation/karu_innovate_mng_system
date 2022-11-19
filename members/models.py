from django.db import models
from users.models import UserModel
# Create your models here.


class Members(models.Model):
    userview = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    reg_no=models.CharField(max_length=100,blank=False,null=False)
    course=models.CharField(max_length=100,blank=False,null=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100,blank=False,null=False)
    last_name=models.CharField(max_length=100,blank=False,null=False)
    class Meta:
        verbose_name_plural='Members'
        db_table='members'
        
    
    
    def __str__(self):
        return self.reg_no
    
    