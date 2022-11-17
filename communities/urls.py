from django.urls import path
from .views import CommunityView
app_name = "communities"

urlpatterns=[
    path('',CommunityView,name='community'),
]