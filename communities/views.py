from django.shortcuts import render
from .models import Community
# Create your views here.
def CommunityView(request):
    community=Community.objects.all()
    context={
        'community':community
    }
    return render(request,'communities/communities.html',context)