from django.contrib import admin
from .models import Films, Seances, Books

# Register your models here.
admin.site.register(Films)
admin.site.register(Seances)
admin.site.register(Books)