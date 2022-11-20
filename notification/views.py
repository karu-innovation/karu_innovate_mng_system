from django.shortcuts import render,reverse,redirect
from .models import Notification
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_gen
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from decouple import config

from members.models import Members
import africastalking
from .forms import EmailForm
from django.conf import settings


username="karatina_university"
api_key = config('AFRICASTALKING_API')
africastalking.initialize(username, api_key)
sms = africastalking.SMS


# Create your views here.
def Notification(request):
    notification=Notification.objects.all()
    members=Members.objects.all()
    emailform=EmailForm()
    if request.method == 'POST':
        message=request.POST.get('message')
        phone_no=request.POST.get('phone_no')
        response = sms.send(message, [phone_no])
        print(response)
        messages.success(request, 'Message sent successfully')
        return redirect('notification:notification')
    if request.method == 'POST':
        emailform=EmailForm(request.POST)
        if emailform.is_valid():
            email=emailform.cleaned_data.get('email')
            subject=emailform.cleaned_data.get('subject')
            message=emailform.cleaned_data.get('message')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
            messages.success(request, 'Email sent successfully')
            return redirect('notification:notification')
         
        
    context={
        'notification':notification,
        
    }
    return render(request,'notification/notification.html',context)