from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
import uuid
# Create your models here.


class Gallery(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    description=models.TextField()
    file=models.FileField(upload_to='files/')
    image=models.ImageField(upload_to='images/')
    cover_image=ImageSpecField(source='image',
                              processors=[ResizeToFill(100,50)],
                              format='JPEG',
                              options={'quality':60})
    timestap=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)

    
    class Meta:
        verbose_name_plural='Gallery'
        db_table='gallery'        