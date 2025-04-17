from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Appointment

def book_appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        service = request.POST['service']
        date = request.POST['date']
        time = request.POST['time']

        Appointment.objects.create(name=name, email=email, service=service, date=date, time=time)

        send_mail(
            'Appointment Confirmation',
            f"Hi {name}, your booking for {service} on {date} at {time} is confirmed!",
            settings.DEFAULT_FROM_EMAIL,
            [email],
        )

        return render(request, 'appointments/success.html')
    return render(request, 'appointments/form.html')


