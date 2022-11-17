from django.urls import path
from .views import MemberView
app_name = "members"
urlpatterns=[
    path('',MemberView,name='member'),
]
