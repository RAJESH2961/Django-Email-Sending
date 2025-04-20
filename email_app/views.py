from django.core.mail import send_mail
from django.http import HttpResponse

def send_simple_email(request):
    subject = 'Test Email'
    message = 'This is a test email.'
    email_from = 'grajesh2906@gmail.com'  # You can use the EMAIL_HOST_USER variable here as well
    recipient = ['grajesh2907@gmail.com']  # Replace with a valid email address
    res = send_mail(subject, message, email_from, recipient)
    return HttpResponse(f"Email sent successfully: {res}")
