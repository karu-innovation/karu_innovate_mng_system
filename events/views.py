from django.shortcuts import render

# Create your views here.
def EventView(request):
    context = {}
    
    return render(request, 'events/events.html', context)