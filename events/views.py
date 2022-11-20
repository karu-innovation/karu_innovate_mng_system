from django.shortcuts import render,redirect
from .models import Events
from .forms import CreateEventForm
# Create your views here.
def EventView(request):
    createEventForm=CreateEventForm()
    events=Events.objects.all()
    if request.method=='POST':
        createEventForm=CreateEventForm(request.POST,request.FILES)
        if createEventForm.is_valid():
            createEventForm.save()
            return redirect('events')
    context = {
        'events': events,
        'createEventForm': createEventForm,
    }
    
    return render(request, 'events/events.html', context)