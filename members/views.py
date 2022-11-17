from django.shortcuts import render

# Create your views here.
def MemberView(request):
    return render(request,'members/member.html')