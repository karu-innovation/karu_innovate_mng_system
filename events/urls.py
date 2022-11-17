from django.urls import path
from .views import EventView
app_name = "events"

urlpatterns=[
    path('',EventView,name='event'),
]

