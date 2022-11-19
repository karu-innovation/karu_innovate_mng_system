from django.urls import path
from .views import Notification
app_name = "notification"

urlpatterns=[
    path('',Notification,name='notification'),
]