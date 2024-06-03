from django.urls import path
from . import views
from .views import booking

urlpatterns = [
    path('', views.poster, name='poster'),
    path('booking', booking.as_view(), name='booking'),
    path('send_email', views.send_email, name='send_email')
]