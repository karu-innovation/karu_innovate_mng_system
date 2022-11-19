from django.urls import path
from .views import AccountUsers
app_name='accountUsers'


urlpatterns=[
    path('',AccountUsers,name='accountUsers'),
]
