from django import forms

from .models import *

class Data111Form(forms.ModelForm):
    class Meta:
        model = Data111
        fields = ['наименование', 'инн', 'огрн', 'код_эмитента']

class Data111EditForm(forms.ModelForm):
	class Meta:
		model = Data111
		fields = ['наименование', 'инн', 'огрн','дата_регистрации','опф','код_эмитента','уставной_капитал', 'количество_лицевых_счетов_в_реестре', 'количество_номинальных_держателей_в_реестре', 'сведения_об_открытии_счета_номинального_держателя_центрального_депозитария', 'регион', 'адрес', 'единоличный_исполнительный_орган', 'контактные_данные', 'статус', 'движение_денежных_средств', 'отчетность', 'задолженность_перед_фнс']