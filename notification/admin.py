from django.contrib import admin
from .models import Notification
# Register your models here.

admin.site.site_header = 'Karatina University'
admin.site.site_title = 'Karatina University'
admin.site.index_title = 'Karatina University'
admin.site.register(Notification)

