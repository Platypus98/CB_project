from django import forms

from .models import *

class Data111Form(forms.ModelForm):
    class Meta:
        model = Data111
        fields = ['наименование', 'инн', 'огрн', 'код_эмитента']
