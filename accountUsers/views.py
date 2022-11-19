from django.shortcuts import render

# Create your views here.

def  AccountUsers(request):
    return render(request,'accountUsers/accountUsers.html')