#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from .models import *

class Data111Form(forms.ModelForm):
    class Meta:
        model = Data111
        fields = ['naimenovanie', 'inn', 'ogrn', 'cod_emitenta']
        labels = {
            "naimenovanie": "Наименование:",
            "inn": "ИНН:",
            "ogrn": "ОГРН:",
            "cod_emitenta": "Код эмитента:",
        }

class Data111EditForm(forms.ModelForm):
	class Meta:
		model = Data111
		fields = ['naimenovanie', 'inn', 'ogrn','data_registracii','opf','cod_emitenta','ustavnoy_capital', 'kolichestvo_licevyh_schetov_v_reestre', 'kolichestvo_nominalnyh_derzhateley_v_reestre', 'cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria', 'region', 'adres', 'edinolichny_ispolnitelny_organ', 'contactny_dannye', 'status', 'dvizhenie_denezhnyh_sredstv', 'otchetnost', 'zadolzhennost_pered_fns']
        labels = {
            "naimenovanie": "Наименование:",
            "inn": "ИНН:",
            "ogrn": "ОГРН:",
            "data_registracii": "Дата регистрации:",
            "opf": "ОПФ:",
            "cod_emitenta": "Код эмитента:",
            "ustavnoy_capital": "Уставной капитал:",
            "kolichestvo_licevyh_schetov_v_reestre": "Количество лицевых счетов в реестре:",
            "kolichestvo_nominalnyh_derzhateley_v_reestre": "Количество номинальных держателей в реестре:",
            "cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria": "Сведения об открытии счета номинального держателя центрального депозитория: ",
            "region": "Регион:",
            "adres": "Адрес:",
            "edinolichny_ispolnitelny_organ": "Единоличный исполнительный орган:",
            "contactny_dannye": "Контактные данные:",
            "status": "Статус:",
            "dvizhenie_denezhnyh_sredstv": "Движение денежных средств:",
            "otchetnost": "Отчетность:",
            "zadolzhennost_pered_fns": "Задолженность перед ФНС:",  
        }