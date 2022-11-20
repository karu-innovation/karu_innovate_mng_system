from django.urls import path
from .views import Event



app_name = "events"

urlpatterns=[
    path('',Event,name='events'),
]

