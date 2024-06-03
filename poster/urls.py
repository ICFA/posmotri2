from django.urls import path
from . import views

urlpatterns = [
    path('', views.poster, name='poster'),
    path('booking', views.booking, name='booking'),
    path('send_email', views.send_email, name='send_email')
]