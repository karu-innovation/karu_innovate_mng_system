from django.shortcuts import render,reverse,redirect
from .models import Notification
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_gen
from django.contrib.auth.tokens import PasswordResetTokenGenerator

import africastalking
from .forms import EmailForm
from django.conf import settings
username="karatina_university"
api_key ="07993e9871f4dbb20cffd923e901839e0c024ba68a7b907fffe4b5d953ec645a"
africastalking.initialize(username, api_key)
sms = africastalking.SMS
# Create your views here.
def Notification(request):
    notification=Notification.objects.all()
    emailform=EmailForm()
    if request.method == 'POST':
        emailform=EmailForm(request.POST)
        if emailform.is_valid():
            emailform.save()
            uidb64 = urlsafe_base64_encode(force_bytes(request.user.pk))
            domain = get_current_site(request).domain
            link = reverse('accounts:activate', 
                            kwargs={
                                'uidb64':uidb64, 
                                'token':token_gen.make_token(user)
                                    })
            activate_url = f"http://{domain+link}"
            
            mail_subject = "Activate your account"

            
            mail_body = f"hi {user.username} click the link below to verify your account\n {activate_url}"
            mail = send_mail (mail_subject, mail_body,'noreply@courses.com',[user.email], fail_silently=False)
            messages.success(request, "Account created, Check your email to activate your account")
            return redirect('accounts:login')
    context={
        'notification':notification
    }
    return render(request,'notification/notification.html',context)