from django import forms
from django.core.exceptions import ValidationError

from .models import (Dvd, Book, Music, Actor)

class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
