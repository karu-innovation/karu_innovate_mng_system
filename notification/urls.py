from django.urls import path
from .views import Notification
app_name = "notifications"

urlpatterns=[
    path('',Notification,name='notification'),
]