from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Events(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(upload_to='images/')
    image=ImageSpecField(source='image',
                         processors=[ResizeToFill(100,50)],
                         options={'quality':60},
                            format='JPEG')                  
    description=models.TextField()
    file=models.FileField(upload_to='files/')
    timestamp=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Events'
        db_table='events'
                        