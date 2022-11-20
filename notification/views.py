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
from .forms import EmailForm,TextForm
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
        emailform=EmailForm(request.POST)
        if emailform.is_valid():
            emailform.save()
            uidb64 = urlsafe_base64_encode(force_bytes(request.user.pk))
            domain = get_current_site(request).domain
            for member in range(len(members)):
                link = reverse('activate', kwargs={
                    'uidb64': uidb64, 'token': token_gen.make_token(request.user)})
                activate_url = 'http://' + domain + link
                subject = 'Activate your account'
                message = 'Hi ' + members[member].first_name + ' ' + members[member].last_name + ' '+ ' with E Mail ' + ' '+ members[member].email + ', please use this link to activate your account \n' + activate_url
                send_mail(subject, message, settings.EMAIL_HOST_USER, [members[member].email], fail_sending=False)
                
                return redirect('notification')
    # if request.method == 'POST':
    #     message=request.POST.get('message')
    #     phone_number=request.POST.get('phone_number')
    #     response = sms.send(message, [phone_number])
    #     print(response)
    #     return redirect ('notification')        
    context={
        'notification':notification,
        'form':EmailForm,
    }
    return render(request,'notification/notification.html',context)