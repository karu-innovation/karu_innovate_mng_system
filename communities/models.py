from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from accountUsers.models import UserModel
from django.utils.text import slugify
# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    lead=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='lead')
    members = models.ManyToManyField(UserModel ,related_name='members')
    cover_image = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='cover_image',
                                     
                                    processors=[ResizeToFill(100, 50)],
                                    format='JPEG',
                                    options={'quality': 60})
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Communities"
        db_table = 'community'
                                        
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Community, self).save(*args, **kwargs)
