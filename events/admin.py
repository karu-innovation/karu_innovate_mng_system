from django.contrib import admin
from .models import Events
# Register your models here.

admin.site.site_header='Admin panel'
admin.site.site_title='Admin panel'


class EventsAdmin(admin.ModelAdmin):
    list_display=('name','image','description','file','category','venue','location','community')
    list_filter=('name','category','community')
    search_fields=('name','category','community')
    list_per_page=10
