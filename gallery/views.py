from django.shortcuts import render

# Create your views here.

def GalleryView(request):
    context={}
    return render (request,'gallery/gallery.html',context)