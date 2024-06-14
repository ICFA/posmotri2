from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    return HttpResponseRedirect('poster/afisha')

def about(request):
    return render(request, "main/about.html")

# def booking(request):
#     return render(request, "main/booking.html")