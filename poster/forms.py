from django import forms
from .models import Films, Seances, Books

class SeancesForm(forms.ModelForm):
    class Meta:
        model = Seances
        fields = '__all__'

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'