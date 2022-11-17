from django.shortcuts import render

# Create your views here.
def CommunityView(request):
    return render(request,'communities/communities.html')