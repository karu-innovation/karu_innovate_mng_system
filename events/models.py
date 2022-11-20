from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from communities.models import Community
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    slug=models.SlugField(max_length=50,blank=False,null=False)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)
class Events(models.Model):
    community=models.ForeignKey(Community,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,blank=False,null=False)
    image=models.ImageField(upload_to='images/')
    image=ImageSpecField(source='image',
                         processors=[ResizeToFill(100,50)],
                         options={'quality':60},
                            format='JPEG')                  
    description=models.TextField()
    file=models.FileField(upload_to='files/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    venue=models.CharField(max_length=100,blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        verbose_name_plural='Events'
        db_table='events'
    
    