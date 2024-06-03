from django.shortcuts import render
from .models import Films, Seances, Books
from .forms import FilmsForm, SeancesForm, BooksForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import CreateView


def poster(request):
    films = Films.objects.order_by('-release_date')
    return render(request, 'main/poster.html', {'films': films})

def booking(request):
    return render(request, 'main/booking.html', {'booking': booking})

class UniAdd(CreateView):
    model = Books
    form_class = BooksForm
    template_name = 'main/booking.html'
    success_url = '/'
    extra_context = {
        'title': 'Забронировать место',
    }

def send_email(request):
    email_to = ['nikitavkola@gmail.com', ]
    send_mail("Тема письма", "Письмо с паролем, пусть будет 12115633", settings.EMAIL_HOST_USER, email_to)
    return render(request, 'main/send_email.html', {'email': email_to[0]})