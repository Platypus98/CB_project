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
class Data111Edit_KartochkaForm(forms.ModelForm):
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

class Data111Edit_Korp_KontrolForm(forms.ModelForm):
    class Meta(object):
        model = Data111
        fields = ['registrator', "data_pisma_po_reestru", "nomer_pisma_po_reestru","data_zaprosa_po_reestru", "nomer_zaprosa_po_reestru", "data_predpisanya_po_reestru", "nomer_predpisaniya_po_reestru", "data_provedeniya_gosa", "data_zaprosa_po_gosa", "nomer_zaprosa_po_gosa", "data_predpisaniya_po_1_vypusku", "nomer_predpisaniya_po_1_vypusku", "nrd", "oao_na_22_06_2015"]
        labels = {
            "registrator": "Регистратор",
            "data_pisma_po_reestru": "Дата письма по реестру",
            "nomer_pisma_po_reestru": "Номер письма по реестру",
            "data_zaprosa_po_reestru": "Дата запроса по реестру",
            "nomer_zaprosa_po_reestru": "Номер запроса по реестру",
            "data_predpisanya_po_reestru": "Дата предписания по реестру", 
            "nomer_predpisaniya_po_reestru": "Номер предписания по реестру",
            "data_provedeniya_gosa": "Дата проведения госа",
            "data_zaprosa_po_gosa": "Дата запроса по госа",
            "nomer_zaprosa_po_gosa": "Номер запроса по госа",
            "data_predpisaniya_po_1_vypusku": "Дата предписания по 1 выпуску", 
            "nomer_predpisaniya_po_1_vypusku": "Номер предписания по 1 выпуску", 
            "nrd": "НРД", 
            "oao_na_22_06_2015": "ОАО на 22.06.2015",
        }
            

class Data111FormSelection(forms.ModelForm):
    naimenovanie = forms.BooleanField(label="Наименование", required=False)
    inn = forms.BooleanField(label="ИНН", required=False)
    ogrn = forms.BooleanField(label="ОГРН", required=False)
    data_registracii = forms.BooleanField(label="Дата регистрации", required=False)
    opf = forms.BooleanField(label="ОПФ", required=False)
    cod_emitenta = forms.BooleanField(label="Код эмитента",required=False)
    ustavnoy_capital = forms.BooleanField(label="Уставной капитал", required=False)
    kolichestvo_licevyh_schetov_v_reestre = forms.BooleanField(label='Количество лицевых счетов в реестре', required=False)
    kolichestvo_nominalnyh_derzhateley_v_reestre = forms.BooleanField(label='Количество номинальных держателей в реестре', required=False)
    cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria = forms.BooleanField(label='Сведения об открытии счета номинального держателя центрального депозитория', required=False)
    region = forms.BooleanField(label='Регион', required=False)
    adres = forms.BooleanField(label='Адрес', required=False)
    edinolichny_ispolnitelny_organ = forms.BooleanField(label='Единоличный исполнительный орган', required=False)
    contactny_dannye = forms.BooleanField(label='Контактные данные', required=False)
    status = forms.BooleanField(label='Статус', required=False)
    dvizhenie_denezhnyh_sredstv = forms.BooleanField(label='Движение денежных средств', required=False)
    otchetnost = forms.BooleanField(label='Отчетность', required=False)
    zadolzhennost_pered_fns = forms.BooleanField(label='Задолженность перед ФНС', required=False)

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
