from django.shortcuts import render

# Create your views here.
def UserView(request):
    return render(request,'users.html')