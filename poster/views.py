from django.shortcuts import render
from .models import Films, Seances, Books
from .forms import SeancesForm, BooksForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic.edit import CreateView


def poster(request):
    films = Films.objects.order_by('-release_date')
    return render(request, 'main/poster.html', {'films': films})

# def booking(request):
#     return render(request, 'main/booking.html', {'booking': booking})

class booking(CreateView):
    model = Books
    form_class = BooksForm
    template_name = 'main/booking.html'
    success_url = 'send_email'
    extra_context = {
        'title': 'Забронировать место',
    }

def send_email(request):
    last_book = Books.objects.reverse()[0]
    email_to = [f'{last_book.mail}', ]
    send_mail("Тема письма", f"Вы заказали билет на {last_book.seanse_number}, ваше место {last_book.seat}", settings.EMAIL_HOST_USER, email_to)
    return render(request, 'main/send_email.html', {'email': email_to[0]})