from django import forms
from django.core.exceptions import ValidationError

from .models import Dvd

class DvdForm(forms.ModelForm):

    class Meta:
        model = Dvd
        fields = '__all__'
