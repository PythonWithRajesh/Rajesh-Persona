from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def home(request):

    context = {}

    if request.method == "POST":

        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:

            full_message = f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
"""

            try:

                send_mail(
                    subject=f"New Contact Form Message from {name}",
                    message=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['rajeshlagdhir07@gmail.com'],
                    fail_silently=False,
                )

                context['success'] = "Message sent successfully!"

            except Exception as e:

                print(e)

                context['error'] = "Failed to send message."

        else:

            context['error'] = "Please fill all required fields."

    return render(request, 'main/index.html', context)