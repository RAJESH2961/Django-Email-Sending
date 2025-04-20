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


#Send email in HTML form with an attachment

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.conf import settings

def send_simple_email(request):
    subject = "🎉 Welcome to DjangoPro - Unlock Your Full Potential!"
    from_email = settings.EMAIL_HOST_USER
    to_email = ['grajesh2906@gmail.com', 'grajesh2907@gmail.com', 'grajesh2961@gmail.com']

    text_content = "Hi Rajesh,\nWelcome to DjangoPro! Explore features, connect, and grow.\nVisit: https://yourdomain.com"

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
                color: #333;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                background-color: #fff;
                border-radius: 10px;
                padding: 30px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .logo {
                text-align: center;
            }
            .logo img {
                height: 60px;
            }
            h1 {
                color: #2E86C1;
            }
            .btn {
                display: inline-block;
                padding: 12px 20px;
                background-color: #2E86C1;
                color: #fff;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 20px;
            }
            .footer {
                margin-top: 30px;
                font-size: 12px;
                color: #888;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">
                <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" alt="Logo">
            </div>
            <h1>Welcome, Rajesh! 🎉</h1>
            <p>Thanks for joining <b>DjangoPro</b> — a powerful platform to learn, build, and grow with Django!</p>
            <p>Here's what you can do right now:</p>
            <ul>
                <li>🔍 Explore our features</li>
                <li>👤 Customize your profile</li>
                <li>🤝 Connect with the community</li>
            </ul>
            <p>
                <a href="https://yourdomain.com/dashboard" class="btn">Visit Your Dashboard</a>
            </p>
            <div class="footer">
                You're receiving this email because you registered at DjangoPro.<br>
                © 2025 DjangoPro Inc. | <a href="#">Unsubscribe</a>
            </div>
        </div>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return HttpResponse("✅ Advanced HTML email sent successfully!")


from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.conf import settings
import os

def send_simple_email(request):
    subject = "📎 Your File is Attached!"
    from_email = settings.EMAIL_HOST_USER
    to_email = ['grajesh2906@gmail.com']
    text_content = "Hello! Please find the attached file below."

    html_content = """
    <html>
    <body>
        <h2>Hi Rajesh 👋,</h2>
        <p>Please find the document attached below.</p>
        <p>Best regards,<br><strong>Django Team</strong></p>
    </body>
    </html>
    """

    # Create email
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")

    # Path to file (make sure it's readable)
    file_path = os.path.join(settings.BASE_DIR, 'files/rajesh2906.pdf')  # e.g., store in /files/ folder
    email.attach_file(file_path)  # Attaches any file

    # Send it
    email.send()

    return HttpResponse("✅ Email with attachment sent successfully!")




#Forms logic to process meil without storing in database
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} <{email}>:\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,#sender
                settings.ADMINS,#Receiver admins 2 members
                fail_silently=False,
            )

            return render(request, 'contactForm/contact_success.html')  # optional
    else:
        form = ContactForm()

    return render(request, 'contactForm/contactform.html', {'form': form})


#storing the form data in database also adding CC and BCC
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage  # Import your model

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage  # Ensure this model exists

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', 'Contact Form Submission')
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save to DB
            ContactMessage.objects.create(
                name=name,
                subject=subject,
                email=email,
                message=message
            )

            # Compose full message
            full_message = f"Message from {name} <{email}>:\n\n{message}"

            # Send email
            email_message = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[admin[1] for admin in settings.ADMINS],  # Only the email from each tuple
                cc=['gbharathi32561@gmail.com'],
                bcc=['162411510201@apollouniversity.edu.in'],
                reply_to=[email],
            )
            email_message.send(fail_silently=False)

            return render(request, 'contactForm/contact_success.html')  # success page
    else:
        form = ContactForm()

    return render(request, 'contactForm/contactform.html', {'form': form})
