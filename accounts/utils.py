from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import EmailMessage
def detect_user(user):
    if user.role == 1:
       redirecturl='vendorDashboard'
       return redirecturl
    elif user.role == 2:
       redirecturl='custDashboard'
       return redirecturl
    elif user.role == None and user.is_superadmin:
       redirecturl='/admin'
       return redirecturl

def send_verification_email(request, user, mail_subject, email_template):
   current_site = get_current_site(request)
   mail_subject='Please activate your account'
   message = render_to_string(email_template,{
      'user':user,
      'domain':current_site,
      'uid':urlsafe_base64_encode(force_bytes(user.pk)),
      'token': default_token_generator.make_token(user),
   })
   to_email = user.email
   # from_email = 'django.foodcourt@gmail.com'
   from_email = settings.DEFAULT_FROM_EMAIL
   print(to_email,"EMAIl")
   mail = EmailMessage(mail_subject, message, from_email=from_email, to=[to_email])
   print(mail,"MAIL")
   mail.send()
