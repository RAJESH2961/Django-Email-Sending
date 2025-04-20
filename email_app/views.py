from django.core.mail import send_mail
from django.http import HttpResponse


#Sending an single mail
def send_simple_email(request):
    subject = 'Test Email'
    message = 'This is a test email.'
    email_from = 'grajesh2906@gmail.com'  # You can use the EMAIL_HOST_USER variable here as well
    recipient = ['grajesh2907@gmail.com']  # Replace with a valid email address
    res = send_mail(subject, message, email_from, recipient)
    return HttpResponse(f"Email sent successfully: {res}")


#sending an multiple mail

from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail
from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.http import HttpResponse
from django.conf import settings

def send_simple_email(request):
    email1 = (
        'Welcome to Django Emailing 🎉',
        'Hi Rajesh,\n\nWe are excited to have you onboard!\nStay tuned for more updates.\n\nRegards,\nDjango Team',
        settings.EMAIL_HOST_USER,
        ['grajesh2906@gmail.com']
    )

    email2 = (
        'Weekly Newsletter 📰',
        'Hello Rajesh,\n\nHere’s your weekly dose of news and tips related to Django development.\n\nHappy Coding!\nTeam Django',
        settings.EMAIL_HOST_USER,
        ['grajesh2907@gmail.com']
    )

    email3 = (
        'Account Activity Notice ⚠️',
        'Hi Rajesh,\n\nWe noticed a new login to your account. If this wasn’t you, please secure your account.\n\nStay safe!\nSecurity Team',
        settings.EMAIL_HOST_USER,
        ['grajesh2961@gmail.com']
    )

    send_mass_mail((email1, email2, email3), fail_silently=False)
    return HttpResponse("✅ All the emails have been sent successfully!")
