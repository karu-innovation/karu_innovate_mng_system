from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from users.models import Users
# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lead=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='lead')
    members = models.ManyToManyField(Users,related_name='members')
    cover_image = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='cover_image',
                                     
                                    processors=[ResizeToFill(100, 50)],
                                    format='JPEG',
                                    options={'quality': 60})
    class Meta:
        verbose_name_plural = "Communities"
        db_table = 'community'
                                        
    
    def __str__(self):
        return self.name