from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def home(request):

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
                    subject="New Contact Form Message",
                    message=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['rajeshlagdhir07@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                return render(request, 'main/index.html', {
                    'error': str(e)
                })

        return redirect(request.path)

    return render(request, 'main/index.html')