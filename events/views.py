from django.shortcuts import render,redirect
from .forms import EventForm
from .models import Events


# Create your views here.
def Event(request):
    eventForm=EventForm()
    events=Events.objects.all()
    if request.method=='POST':
        eventForm=EventForm(request.POST,request.FILES)
        if eventForm.is_valid():
            eventForm.save()
            return redirect('events')
    context = {
        'events': events,
        'eventForm': eventForm,
    }
    
    return render(request, 'events/events.html', context)