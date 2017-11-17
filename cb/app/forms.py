from django import forms

from .models import *

class Data111Form(forms.Form):
    naimen = forms.CharField(label='Наименование', max_length=100)
    inn = forms.CharField(label='ИНН', max_length=100)
    code = forms.CharField(label='Код эмитенты', max_length=100)
