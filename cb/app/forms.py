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
        fields = ['naimenovanie', 'inn', 'ogrn','data_registracii','opf','cod_emitenta','ustavnoy_capital', 'kolichestvo_licevyh_schetov_v_reestre', 'kolichestvo_nominalnyh_derzhateley_v_reestre', 'cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria', 'region', 'adres', 'edinolichny_ispolnitelny_organ', 'contactny_dannye', 'status', 'dvizhenie_denezhnyh_sredstv', 'otchetnost', 'zadolzhennost_pered_fns', 'kpp']
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
            "kpp": "КПП"
        }

class Data111Edit_Korp_KontrolForm(forms.ModelForm):
    class Meta(object):
          model = Data111
          fields = ['registrator', "data_pisma_po_reestru", "nomer_pisma_po_reestru","data_zaprosa_po_reestru",
                     "nomer_zaprosa_po_reestru", "data_predpisanya_po_reestru", "nomer_predpisaniya_po_reestru", 
                     "data_provedeniya_gosa", "data_zaprosa_po_gosa", "nomer_zaprosa_po_gosa", "data_predpisaniya_po_1_vypusku", 
                     "nomer_predpisaniya_po_1_vypusku", "nrd", "oao_na_22_06_2015"]
          labels = {    "registrator": "Реестр передан:",
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

          widgets = {
                        'registrator': forms.RadioSelect()
                      }

class Data111Edit_Raskrytie(forms.ModelForm):
    class Meta(object):
        model = Data111
        fields = ['pao_v_silu_priznakov', 'pao_v_silu_nazvaniya', 'nao_obyazannoe_raskryvat_informaciyu_v_sootvetstvii_so_st_30_fz_o_pcb', 'nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag',
                'nao','otkaz_v_registracii_vipuska', 'osvobozhdeny_ot_raskrytiya', 'data_resheniya_ob_osvobozhdenii', 'nomer_resheniya_ob_osvobozhdenii','otkaz_v_osvobozhdenii_ot_raskritiya', 'data_otkaza_v_osvobozhdenii_ot_raskritiya',
                'nomer_otkaza_v_osvobozhdenii_ot_raskritiya', 'proverka_raskritiya', 'data_proverki', 'data_zaprosa_po_neraskritiyu_informacii', 'nomer_zaprosa_po_neraskritiyu_informacii',
                'data_predpisaniya_po_neraskritiyu_informacii','nomer_predpisaniya_po_neraskritiyu_informacii', 'data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve', 'nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve',
                'data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','vivod']
        labels = {
            'pao_v_silu_priznakov': 'ПАО в силу признаков',
            'pao_v_silu_nazvaniya': 'ПАО в силу названия',
            'nao_obyazannoe_raskryvat_informaciyu_v_sootvetstvii_so_st_30_fz_o_pcb': 'НАО обязанное раскрывать информацию в соответствии со ст.30 ФЗ о РЦБ',
            'nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag': 'НАО осуществившее (осуществляющее) публичное размещение облигаций или иных ценных бумаг',
            'nao':'НАО',
            'otkaz_v_registracii_vipuska': 'Отказ в регистрации выпуска',
            'osvobozhdeny_ot_raskrytiya': 'Освобождены от раскрытия',
            'data_resheniya_ob_osvobozhdenii':'Дата решения об освобождении',
            'nomer_resheniya_ob_osvobozhdenii': 'Номер решения об освобождении',
            'otkaz_v_osvobozhdenii_ot_raskritiya': 'Отказ в освобождении от раскрытия',
            'data_otkaza_v_osvobozhdenii_ot_raskritiya': 'Дата отказа в освобождении от раскрытия',
            'nomer_otkaza_v_osvobozhdenii_ot_raskritiya': 'Номер отказа в освобождении от раскрытия',
            'proverka_raskritiya': 'Проверка раскрытия',
            'data_proverki': 'Дата проверки',
            'data_zaprosa_po_neraskritiyu_informacii':'Дата запроса по нераскрытию информации',
            'nomer_zaprosa_po_neraskritiyu_informacii': 'Номер запроса по нераскрытию информации',
            'data_predpisaniya_po_neraskritiyu_informacii': 'Дата предписания по нераскрытию информации',
            'nomer_predpisaniya_po_neraskritiyu_informacii': 'Номер предписания по нераскрытию информации',
            'data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve': 'Дата запроса о результатах проведения торгов в обществе',
            'nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve': 'Номер запроса о результатах проведения торгов в обществе',
            'data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve': 'Дата ответа на запрос о результатах проведения торгов в обществе',
            'nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve': 'Номер ответа на запрос о результатах проведения торгов в обществе',
            'vivod': 'Вывод',
        }
            

class Data111Edit_Administrativka(forms.ModelForm):
    class Meta(object):
        model = Data111
        fields = ['data_protokola','nomer_protokola','statya_koap','data_postanovleniya','nomer_postanovleniya','resultat','razmer_shtrafa']
        labels = {
        'data_protokola': 'Дата протокола',
        'nomer_protokola': 'Номер протокола',
        'statya_koap': 'Статья КОАП',
        'data_postanovleniya': 'Дата постановления',
        'nomer_postanovleniya': 'Номер постановления',
        'resultat': 'Результат',
        'razmer_shtrafa': 'Размер штрафа',
        }
            
        
class Data111Edit_Vzaimodeystvie(forms.ModelForm):
    class Meta(object):
        model = Data111
        fields = ['fns','data_pisma_v_fns','nomer_pisma_v_fns','informaciya_o_poluchenii_otveta_ot_fns','vh_nomer_otveta','soderzhanie_otveta','otvet_fns_ob_adrese','vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove','vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_nomer_pisma','vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_data_pisma','svedeniya_ob_adrese_ne_dostoverny','data_vneseniya_zapisi']
        labels = {
        'fns': 'ФНС',
        'data_pisma_v_fns': 'Дата письма в ФНС',
        'nomer_pisma_v_fns': 'Номер письма в ФНС',
        'informaciya_o_poluchenii_otveta_ot_fns': 'Информация о получении ответа от ФНС',
        'vh_nomer_otveta': 'Вх. номер ответа',
        'soderzhanie_otveta': 'Содержание ответа',
        'otvet_fns_ob_adrese': 'Ответ ФНС об адресе',
        'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove':'Взаимодействие с ФНС на ежеквартальной основе',
        'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_nomer_pisma':'Взаимодействие с ФНС на ежеквартальной основе (номер письма)',
        'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_data_pisma':'Взаимодействие с ФНС на ежеквартальной основе (дата письма)',
        'svedeniya_ob_adrese_ne_dostoverny': 'Сведения об адресе не достоверны',
        'data_vneseniya_zapisi': 'Дата внесения записи',
        }
            
        
            

class Data111FormSelection(forms.ModelForm):
    naimenovanie = forms.BooleanField(label="НАИМЕНОВАНИЕ", required= True, initial=False)
    inn = forms.BooleanField(label="ИНН", required=False, initial=False )
    ogrn = forms.BooleanField(label="ОГРН", required=False, initial=False)
    kpp = forms.BooleanField(label="КПП", required=False, initial=False)
    data_registracii = forms.BooleanField(label="ДАТА РЕГИСТРАЦИИ", required=False, initial=False)
    opf = forms.BooleanField(label="ОПФ", required=False)
    cod_emitenta = forms.BooleanField(label="КОД ЭМИТЕНТА",required=False)
    ustavnoy_capital = forms.BooleanField(label="УСТАВНОЙ КАПИТАЛ", required=False)
    kolichestvo_licevyh_schetov_v_reestre = forms.BooleanField(label='КОЛИЧЕСТВО ЛИЦЕВЫХ СЧЕТОВ В РЕЕСТРЕ', required=False)
    kolichestvo_nominalnyh_derzhateley_v_reestre = forms.BooleanField(label='КОЛИЧЕСТВО НОМИНАЛЬНЫХ ДЕРЖАТЕЛЕЙ В РЕЕСТРЕ', required=False)
    cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria = forms.BooleanField(label='СВЕДЕНИЯ ОБ ОТКРЫТИИ СЧЕТА НОМИНАЛЬНОГО ДЕРЖАТЕЛЯ ЦЕНТРАЛЬНОГО ДЕПОЗИТОРИЯ', required=False)
    region = forms.BooleanField(label='РЕГИОН', required=False)
    adres = forms.BooleanField(label='АДРЕС', required=False)
    edinolichny_ispolnitelny_organ = forms.BooleanField(label='ЕДИНОЛИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ ОРГАН', required=False)
    contactny_dannye = forms.BooleanField(label='КОНТАКТНЫЕ ДАННЫЕ', required=False)
    status = forms.BooleanField(label='СТАТУС', required=False)
    dvizhenie_denezhnyh_sredstv = forms.BooleanField(label='ДВИЖЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ', required=False)
    otchetnost = forms.BooleanField(label='ОТЧЕТНОСТЬ', required=False)
    zadolzhennost_pered_fns = forms.BooleanField(label='ЗАДОЛЖЕННОСТЬ ПЕРЕД ФНС', required=False)
    
    registrator = forms.BooleanField(label="РЕГИСТРАТОР", required=False)  
    naimenovanie_registratora = forms.BooleanField(label="НАИМЕНОВАНИЕ РЕГИСТРАТОРА", required=False)
    data_pisma_po_reestru = forms.BooleanField(label="ДАТА ПИСЬМА ПО РЕЕСТРУ", required=False)  
    nomer_pisma_po_reestru = forms.BooleanField(label="НОМЕР ПИСЬМА ПО РЕЕСТРУ", required=False)  
    data_zaprosa_po_reestru = forms.BooleanField(label="ДАТА ЗАПРОСА ПО РЕЕСТРУ", required=False)
    nomer_zaprosa_po_reestru = forms.BooleanField(label="НОМЕР ЗАПРОСА ПО РЕЕСТРУ", required=False)
    data_predpisanya_po_reestru = forms.BooleanField(label="ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ", required=False)
    nomer_predpisaniya_po_reestru = forms.BooleanField(label="НОМЕР ПРЕДПИСАНИЯ ПО РЕЕСТРУ", required=False)
    data_provedeniya_gosa = forms.BooleanField(label="ДАТА ПРОВЕДЕНИЯ ГОСА", required=False)
    data_zaprosa_po_gosa = forms.BooleanField(label="ДАТА ЗАПРОСА ПО ГОСА", required=False)
    nomer_zaprosa_po_gosa = forms.BooleanField(label="НОМЕР ЗАПРОСА ПО ГОСА", required=False)
    proverka_1_vipusk = forms.BooleanField(label="ПРОВЕРКА 1 ВЫПУСК", required=False)
    data_predpisaniya_po_1_vypusku = forms.BooleanField(label="ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ", required=False)
    nomer_predpisaniya_po_1_vypusku = forms.BooleanField(label="НОМЕР ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ", required=False)
    nrd = forms.BooleanField(label="НРД", required=False)
    proverki_nrd = forms.BooleanField(label="ПРОВЕРКИ НРД", required=False)
    oao_na_22_06_2015 = forms.BooleanField(label="ОАО НА 22.06.2015", required=False)
    
    pao_v_silu_priznakov = forms.BooleanField(label="ПАО В СИЛУ ПРИЗНАКОВ", required=False)
    pao_v_silu_nazvaniya = forms.BooleanField(label="ПАО В СИЛУ НАЗВАНИЯ", required=False)
    nao_obyazannoe_raskryvat_informaciyu_v_sootvetstvii_so_st_30_fz_o_pcb = forms.BooleanField(label="НАО ОБЯЗАННОЕ РАСКРЫВАТЬ ИНФОРМАЦИЮ В СООТВЕТСТВИИ СО СТ. 30 ФЗ О РЦБ", required=False)
    nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag = forms.BooleanField(label="НАО ОСУЩЕСТВИВШЕЕ (ОСУЩЕСТВЛЯЮЩЕЕ) ПУБЛИЧНОЕ РАЗМЕЩЕНИЕ ОБЛИГАЦИЙ ИЛИ ИНЫХ ЦЕННЫХ БУМАГ", required=False)
    otkaz_v_registracii_vipuska = forms.BooleanField(label="ОТКАЗ В РЕГИСТРАЦИИ ВЫПУСКА", required=False)
    nao = forms.BooleanField(label="НАО", required=False)
    osvobozhdeny_ot_raskrytiya = forms.BooleanField(label="ОСВОБОЖДЕНЫ ОТ РАСКРЫТИЯ", required=False)
    data_resheniya_ob_osvobozhdenii = forms.BooleanField(label="ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ", required=False)
    nomer_resheniya_ob_osvobozhdenii = forms.BooleanField(label="НОМЕР РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ", required=False)
    otkaz_v_osvobozhdenii_ot_raskritiya = forms.BooleanField(label="ОТКАЗ В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ", required=False) 
    data_otkaza_v_osvobozhdenii_ot_raskritiya = forms.BooleanField(label="ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ", required=False) 
    nomer_otkaza_v_osvobozhdenii_ot_raskritiya = forms.BooleanField(label="НОМЕР ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ", required=False)
    proverka_raskritiya = forms.BooleanField(label="ПРОВЕРКА РАСКРЫТИЯ", required=False) 
    data_proverki = forms.BooleanField(label="ДАТА ПРОВЕРКИ", required=False)
    data_zaprosa_po_neraskritiyu_informacii = forms.BooleanField(label="ДАТА ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ", required=False)
    nomer_zaprosa_po_neraskritiyu_informacii = forms.BooleanField(label="НОМЕР ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ", required=False) 
    data_predpisaniya_po_neraskritiyu_informacii = forms.BooleanField(label="ДАТА ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ", required=False) 
    nomer_predpisaniya_po_neraskritiyu_informacii = forms.BooleanField(label="НОМЕР ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ", required=False)  
    data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = forms.BooleanField(label="ДАТА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ", required=False)
    nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = forms.BooleanField(label="НОМЕР ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ", required=False)
    data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = forms.BooleanField(label="ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ", required=False)
    nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = forms.BooleanField(label="НОМЕР ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ", required=False)  
    vivod = forms.BooleanField(label="ВЫВОД", required=False)
    raskritie = forms.BooleanField(label="РАСКРЫТИЕ", required=False)
    
    data_protokola = forms.BooleanField(label="ДАТА ПРОТОКОЛА", required=False)
    nomer_protokola = forms.BooleanField(label="НОМЕР ПРОТОКОЛА", required=False)
    statya_koap = forms.BooleanField(label="СТАТЬЯ КОАП", required=False)
    data_postanovleniya = forms.BooleanField(label="ДАТА ПОСТАНОВЛЕНИЯ", required=False)
    nomer_postanovleniya = forms.BooleanField(label="НОМЕР ПОСТАНОВЛЕНИЯ", required=False)
    resultat = forms.BooleanField(label="РЕЗУЛЬТАТ", required=False)
    razmer_shtrafa = forms.BooleanField(label="РАЗМЕР ШТРАФА", required=False)
    administrativka = forms.BooleanField(label="АДМИНИСТРАТИВКА", required=False)
    
    fns = forms.BooleanField(label="ФНС", required=False) 
    data_pisma_v_fns = forms.BooleanField(label="ДАТА ПИСЬМА В ФНС", required=False)
    nomer_pisma_v_fns = forms.BooleanField(label="НОМЕР ПИСЬМА В ФНС", required=False)
    informaciya_o_poluchenii_otveta_ot_fns = forms.BooleanField(label="ИНФОРМАЦИЯ О ПОЛУЧЕНИИ ОТВЕТА ОТ ФНС", required=False)  
    vh_nomer_otveta = forms.BooleanField(label="ВХ. НОМЕР ОТВЕТА", required=False)  
    
    soderzhanie_otveta = forms.BooleanField(label="СОДЕРЖАНИЕ ОТВЕТА", required=False)
    otvet_fns_ob_adrese = forms.BooleanField(label="ОТВЕТ ФНС ОБ АДРЕСЕ", required=False)
    vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove = forms.BooleanField(label="ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ", required=False)
    vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_nomer_pisma = forms.BooleanField(label="ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (НОМЕР ПИСЬМА)", required=False)
    vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_data_pisma = forms.BooleanField(label="ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (ДАТА ПИСЬМА)", required=False)

    svedeniya_ob_adrese_ne_dostoverny = forms.BooleanField(label="СВЕДЕНИЯ ОБ АДРЕСЕ НЕ ДОСТОВЕРНЫ", required=False)
    data_vneseniya_zapisi = forms.BooleanField(label="ДАТА ВНЕСЕНИЯ ЗАПИСИ", required=False)
    vzaimodeystvie_s_gos_organami = forms.BooleanField(label="ВЗАИМОДЕЙСТВИЕ С ГОС. ОРГАНАМИ", required=False)
    export = forms.BooleanField(label='Выгрузка в XML', required=False)

    class Meta:
        model = Data111
        fields = ['naimenovanie', 'inn', 'ogrn','kpp','data_registracii','opf','cod_emitenta','ustavnoy_capital', 
                  'kolichestvo_licevyh_schetov_v_reestre', 'kolichestvo_nominalnyh_derzhateley_v_reestre', 
                  'cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria', 'region', 
                  'adres', 'edinolichny_ispolnitelny_organ', 'contactny_dannye', 'status', 'dvizhenie_denezhnyh_sredstv', 
                  'otchetnost', 'zadolzhennost_pered_fns', 'registrator', 'naimenovanie_registratora', 'data_pisma_po_reestru', 'nomer_pisma_po_reestru', 
                  'data_zaprosa_po_reestru', 'nomer_zaprosa_po_reestru', 'data_predpisanya_po_reestru', 
                  'nomer_predpisaniya_po_reestru', 'data_provedeniya_gosa', 'data_zaprosa_po_gosa', 
                  'nomer_zaprosa_po_gosa','proverka_1_vipusk', 'data_predpisaniya_po_1_vypusku','nomer_predpisaniya_po_1_vypusku', 
                  'nrd', 'proverki_nrd', 'oao_na_22_06_2015', 'pao_v_silu_priznakov', 'pao_v_silu_nazvaniya', 
                  'nao_obyazannoe_raskryvat_informaciyu_v_sootvetstvii_so_st_30_fz_o_pcb', 
                  'nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag', 
                  'nao', 'otkaz_v_registracii_vipuska','osvobozhdeny_ot_raskrytiya', 'data_resheniya_ob_osvobozhdenii','nomer_resheniya_ob_osvobozhdenii',
                  'otkaz_v_osvobozhdenii_ot_raskritiya','data_otkaza_v_osvobozhdenii_ot_raskritiya', 'nomer_otkaza_v_osvobozhdenii_ot_raskritiya', 
                  'proverka_raskritiya', 'data_proverki', 'data_zaprosa_po_neraskritiyu_informacii', 
                  'nomer_zaprosa_po_neraskritiyu_informacii', 'data_predpisaniya_po_neraskritiyu_informacii', 
                  'nomer_predpisaniya_po_neraskritiyu_informacii', 'data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve',
                  'nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve', 
                  'nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','vivod', 'raskritie', 'data_protokola', 'nomer_protokola', 
                  'statya_koap','data_postanovleniya','nomer_postanovleniya', 'resultat', 'razmer_shtrafa','administrativka','fns', 
                  'data_pisma_v_fns', 'nomer_pisma_v_fns', 'informaciya_o_poluchenii_otveta_ot_fns', 'vh_nomer_otveta', 
                  'soderzhanie_otveta', 'otvet_fns_ob_adrese', 'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove', 'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_nomer_pisma', 'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_data_pisma','svedeniya_ob_adrese_ne_dostoverny', 'data_vneseniya_zapisi', 'vzaimodeystvie_s_gos_organami']
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
            "pao_v_silu_priznakov": "ПАО в силу признаков",
            "pao_v_silu_nazvaniya": "ПАО в силу названия",
            "nao_obyazannoe_raskryvat_informaciyu_v_sootvetstvii_so_st_30_fz_o_pcb": "НАО обязанное раскрывать информацию в соответствии со ст. 30 ФЗ о РЦБ",
            "nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag": "НАО осуществившее (осуществляющее) публичное размещение облигаций или иных ценных бумаг",
            "nao": "НАО",
            "osvobozhdeny_ot_raskrytiya": "Освобождены от раскрытия",
            "data_resheniya_ob_osvobozhdenii": "Дата решения об освобождении",
            "nomer_resheniya_ob_osvobozhdenii": "Номер решения об освобождении",
            "otkaz_v_osvobozhdenii_ot_raskritiya": "Отказ в освобождении от раскрытия",
            "data_otkaza_v_osvobozhdenii_ot_raskritiya": "Дата отказа в освобождении от раскрытия",
            "nomer_otkaza_v_osvobozhdenii_ot_raskritiya": "Номер отказа в освобождении от раскрытия",
            "proverka_raskritiya": "Проверка раскрытия",
            "data_proverki": "Дата проверки",
            "data_zaprosa_po_neraskritiyu_informacii": "Дата запроса по нераскрытию информации",
            "nomer_zaprosa_po_neraskritiyu_informacii": "Номер запроса по нераскрытию информации",
            "data_predpisaniya_po_neraskritiyu_informacii": "Дата предписания по нераскрытию информации",
            "nomer_predpisaniya_po_neraskritiyu_informacii": "Номер предписания по нераскрытию информации",
            "data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve": "Дата запроса о результатах проведения торгов в обществе",
            "nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve": "Номер запроса о результатах проведения торгов в обществе",
            "data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve": "Дата ответа на запроса о результатах проведения торгов в обществе",
            "nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve": "Номер ответа на запроса о результатах проведения торгов в обществе",
            "vivod": "Вывод",
            "raskritie": "Раскрытие",
            "data_protokola": "Дата протокола",
            "nomer_protokola": "Номер протокола",
            "statya_koap": "Статья КОАП",
            "data_postanovleniya": "Дата постановления",
            "nomer_postanovleniya": "Номер постановления",
            "resultat": "Результат",
            "razmer_shtrafa": "Размер штрафа",
            "administrativka": "Административка",
            "fns": "ФНС",
            "data_pisma_v_fns": "Дата письма в ФНС",
            "nomer_pisma_v_fns": "Номер письма в ФНС",
            "informaciya_o_poluchenii_otveta_ot_fns": "Информация о получении ответа от ФНС",
            "vh_nomer_otveta": "Вх. номер ответа",
            "svedeniya_ob_adrese_ne_dostoverny": "Сведения об адресе не достоверны",
            "data_vneseniya_zapisi": "Дата внесения записи",
            "vzaimodeystvie_s_gos_organami": "Взаимодействие с гос. органами",

        }
