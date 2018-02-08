from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from pandas import *

from django.shortcuts import render, redirect

import json

from django.shortcuts import get_object_or_404
from django.contrib import messages

from .forms import *
from .models import *


import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str

import xlwt
from django.db import connection
from collections import namedtuple

import os




# Create your views here.

def search(request):
        form = Data111Form(request.POST or None)
        queryset = None
        context = {
        "queryset": queryset,
        "form": form,
        }
        if request.method == 'POST':
                if form['naimenovanie'].value() == '' and form['inn'].value() == '' and form['ogrn'].value() == '' and form['cod_emitenta'].value() == '':
                        queryset = None
                else:
                        queryset = Data111.objects.all().filter(naimenovanie__icontains = form['naimenovanie'].value(), inn__icontains = form['inn'].value(), ogrn__icontains = form['ogrn'].value(), cod_emitenta__icontains = form['cod_emitenta'].value())
                context = {
            "queryset": queryset,
            "form": form,
            }
        return render(request, 'search.html', context)


def edit_kartochka(request, id):
    title = Data111.objects.get(id = id).naimenovanie
    obj = get_object_or_404(Data111, id = id)
    form = Data111Edit_KartochkaForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        form.save()

    context = {
        "title": title,
        "form": form,
        "id": id,
    }
    return render(request, 'edit_kartochka.html', context)

def edit_korp_kontrol(request, id):
    noblock = False
    sami = False
    net = False
    naimenovanie_reg = True
    otslezhivanie = False
    otslezhivanie1 = False
    index = False
    title = Data111.objects.get(id = id).naimenovanie
    obj = get_object_or_404(Data111, id = id)
    form = Data111Edit_Korp_KontrolForm(request.POST or None, instance=obj)
    if request.method == 'GET':
            if form['registrator1'].value() == 'НЕТ':
                 noblock = True
            if form['netsami'].value() == 'САМИ В ЕГРЮЛ':
                 sami = True
            if form['netsami'].value()  is None:
                 index = True
            if form['netsami'].value() == '---':
                 index = True     
            if form['netsami'].value() == 'НЕТ В ЕГРЮЛ':
                 net = True
            if form['registrator1'].value() == 'НЕТ':
                 naimenovanie_reg = False
            #if form['nomer_zaprosa_po_reestru'].value() is not None:
            #     otslezhivanie = True
            #if form['nomer_predpisaniya_po_reestru'].value() is not None:
            #     otslezhivanie1 = True      

    if request.method == 'POST': 
            if form['registrator1'].value() == 'НЕТ':
                 noblock = True
            if form['netsami'].value() == 'САМИ В ЕГРЮЛ':
                 sami = True 
            if form['netsami'].value()  is None:
                 index = True
            if form['netsami'].value() == '---':
                 index = True             
            if form['netsami'].value() == 'НЕТ В ЕГРЮЛ':
                 net = True 
            if form['registrator1'].value() == 'НЕТ':
                 naimenovanie_reg = False 
            #if form['nomer_zaprosa_po_reestru'].value() is not None:
            #     otslezhivanie = True
            #if form['nomer_predpisaniya_po_reestru'].value() is not None:
            #     otslezhivanie1 = True                  
            if form.is_valid(): 
                 form.save()
    
    context = {
        "title": title,
        "form": form,
        "id": id,
        "noblock": noblock,
        "sami":sami,
        "net":net,
        "naimenovanie_reg":naimenovanie_reg,
        "otslezhivanie":otslezhivanie,
        "index":index,
        "otslezhivanie1":otslezhivanie1,
    }

    return render(request, 'edit_korp_kontrol.html', context)

def edit_raskrytie(request, id):
  title = Data111.objects.get(id = id).naimenovanie
  obj = get_object_or_404(Data111, id = id)
  form = Data111Edit_Raskrytie(request.POST or None, instance=obj)
  if request.method == 'POST':
    form.save()
  context = {
    "title": title,
    "form": form,
    "id": id,
  }
  return render(request, 'edit_raskrytie.html', context)

def edit_administrativka(request, id):
  title = Data111.objects.get(id = id).naimenovanie
  obj = get_object_or_404(Data111, id = id)
  form = Data111Edit_Administrativka(request.POST or None, instance=obj)
  if request.method == 'POST':
    form.save()
  context = {
    "title": title,
    "form": form,
    "id": id,
  }
  return render(request, 'edit_administrativka.html', context)


def edit_vzaimodeystvie(request, id):
  title = Data111.objects.get(id = id).naimenovanie
  obj = get_object_or_404(Data111, id = id)
  form = Data111Edit_Vzaimodeystvie(request.POST or None, instance=obj)
  if request.method == 'POST':
    form.save()
  context = {
  'title': title,
  'form': form,
  'id': id,
  }
  return render(request, 'edit_vzaimodeystvie.html', context)

def selections(request):
        a = []
        b = []
        c = []
        opf = []
        queryset = Data111.objects.all()

        columns_to_display = ['naimenovanie', 'inn', 'ogrn','kpp','data_registracii','opf','cod_emitenta','ustavnoy_capital', 
                  'kolichestvo_licevyh_schetov_v_reestre', 'kolichestvo_nominalnyh_derzhateley_v_reestre', 
                  'cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria', 'region', 
                  'adres', 'edinolichny_ispolnitelny_organ', 'contactny_dannye', 'status', 'dvizhenie_denezhnyh_sredstv', 
                  'data_posledney_operacii', 'otchetnost', 'zadolzhennost_pered_fns', 'registrator', 'naimenovanie_registratora', 'data_pisma_po_reestru', 'nomer_pisma_po_reestru', 
                  'data_zaprosa_po_reestru', 'nomer_zaprosa_po_reestru', 'data_predpisanya_po_reestru', 
                  'nomer_predpisaniya_po_reestru', 'data_provedeniya_gosa', 'data_zaprosa_po_gosa', 
                  'nomer_zaprosa_po_gosa','proverka_1_vipusk', 'data_predpisaniya_po_1_vypusku','nomer_predpisaniya_po_1_vypusku', 
                  'nrd', 'proverki_nrd', 'oao_na_22_06_2015', 'pao_v_silu_priznakov_st30', 'pao_v_silu_priznakov_bez_st30','pao_v_silu_nazvaniya_st30', 
                  'pao_v_silu_nazvaniya_bez_st30','nao_so_st30', 
                  'nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag', 
                  'nao_bez_st30', 'data_opredelenia_statusa', 'otkaz_v_registracii_vipuska','osvobozhdeny_ot_raskrytiya', 'data_resheniya_ob_osvobozhdenii','nomer_resheniya_ob_osvobozhdenii',
                  'otkaz_v_osvobozhdenii_ot_raskritiya','data_otkaza_v_osvobozhdenii_ot_raskritiya', 'nomer_otkaza_v_osvobozhdenii_ot_raskritiya', 
                  'proverka_raskritiya', 'data_proverki', 'data_zaprosa_po_neraskritiyu_informacii', 
                  'nomer_zaprosa_po_neraskritiyu_informacii', 'data_predpisaniya_po_neraskritiyu_informacii', 
                  'nomer_predpisaniya_po_neraskritiyu_informacii', 'data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve',
                  'nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve', 
                  'nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','vivod', 'raskritie', 'data_protokola', 'nomer_protokola', 
                  'statya_koap','data_postanovleniya','nomer_postanovleniya', 'resultat', 'razmer_shtrafa','administrativka','fns', 
                  'data_pisma_v_fns', 'nomer_pisma_v_fns', 'informaciya_o_poluchenii_otveta_ot_fns', 'vh_nomer_otveta', 
                  'soderzhanie_otveta', 'otvet_fns_ob_adrese', 'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove', 'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_nomer_pisma', 'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_data_pisma','svedeniya_ob_adrese_ne_dostoverny', 'data_vneseniya_zapisi', 'vzaimodeystvie_s_gos_organami']

        form = Data111FormSelection(request.POST or None)
        form_filter_opf = Filter_opf(request.POST or None)
        context = {
        "form": form,
        "queryset": queryset,
        "form_filter_opf": form_filter_opf,

        }


#Отображение в браузере
        if request.method == 'POST':

                table_headers = map(lambda a: Data111._meta.get_field(a).help_text or a, columns_to_display)

                for i in form._meta.fields:      
                        if form[i].value(): 
                             a.append(form[i].label)

                for i in form._meta.fields:      
                        if form[i].value(): 
                             b.append(i)


                c = ['row.'+x for x in b]


                #Фильтры ОПФ
                #if form['opf'].value():
                #   for i in ['ao','aozt', 'aoot', 'zao', 'nao', 'oao', 'pao']:
                #       if form_filter_opf[i].value():
                #           table_rows = Data111.objects.filter(opf__exact=form_filter_opf[i].label)
                
                #table_rows = Data111.objects.filter(opf__exact=form_filter_opf[opf[0]].label)
                #table_rows = Data111.objects.filter(opf__exact=form_filter_opf[opf[0]].label)


                table_rows = Data111.objects.all().values(*b)
                
                #a.remove('Export to CSV')  

                context = {
                "form": form,
                        "a": a,
                        "b":b,
                        "c":c,
                        "table_rows": table_rows,
                        "table_headers": table_headers,
                        "queryset": queryset,
                "form_filter_opf": form_filter_opf,
            }
            

#Экспорт в Excel
        if form['export'].value() == True:

            response = HttpResponse(content_type='application/ms-excel')
            
            response['Content-Disposition'] = 'attachment; filename=selection.xls'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet("Data111")

            row_num = 0

            columns = a

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num])
            
                

            font_style = xlwt.XFStyle()
            font_style.alignment.wrap = 1
            
            for obj in queryset:
                row_num += 1
                row = []
                for i in b:
                    row.append(getattr(obj, i))

                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)
                    
            wb.save(response)
            return response
#Конец экспорта в Excel

        return render(request, 'selections.html', context)


def home(request):
    title = 'Добро пожаловать!'
    context = {
        "title": title,
    }
    return render(request, "base.html",context)




#ОБНОВА БД---------_________-------__________---------_______


def namedtuplefetchall(cursor):
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]




def custom_column_query_select(column):
      cursor = connection.cursor()

      cursor.execute("SELECT {} FROM Data111".format(column))

      custom_column = namedtuplefetchall(cursor)

      cursor.close()

      return custom_column


def orgn_query_select(column):
      cursor = connection.cursor()

      cursor.execute("SELECT ОГРН FROM Data111 WHERE {} != 000".format(column))

      ogrn = namedtuplefetchall(cursor)

      cursor.close()

      return ogrn      

def custom_columns_query_insert(column):
      cursor = connection.cursor()

      custom = custom_column_query_select('НЕТСАМИ')

      ogrn = orgn_query_select('НЕТСАМИ')

      for i in range(len(ogrn)):
        cursor.execute('INSERT INTO Data111 ({}) VALUES ({}) WHERE ОГРН = ({})'.format(column,custom[i][0], ogrn[i][0]))

      cursor.close()

        


def delete_db_query():
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Data111 WHERE id >= (SELECT min(id) FROM Data111)")

    cursor.close()



def update_db_query(dict):
    cursor = connection.cursor()

    for i in dict['ОГРН'].keys():
          #cursor.execute('INSERT INTO Data111 (НАИМЕНОВАНИЕ,ИНН,ОГРН,КПП,ДАТА РЕГИСТРАЦИИ,ОПФ,КОД ЭМИТEHТA,УСТАВНЫЙ КАПИТАЛ,Количество лицевых счетов в реестре,Количество номинальных держателей в реестре,Сведения об открытии счета номинального держателя центрального депозитария,РЕГИОН,АДРЕС,ЕДИНОЛИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ ОРГАН,КОНТАКТНЫЕ ДАННЫЕ,СТАТУС,ДВИЖЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ,ДАТА ПОСЛЕДНЕЙ ОПЕРАЦИИ,ОТЧЕТНОСТЬ,ЗАДОЛЖЕННОСТЬ ПЕРЕД ФНС,КАРТОЧКА КОМПАНИИ,РЕГИСТРАТОР,РЕГИСТРАТОР1,НАИМЕНОВАНИЕ РЕГИСТРАТОРА,ДАТА ПИСЬМА ПО РЕЕСТРУ,НОМЕР ПИСЬМА ПО РЕЕСТРУ,ДАТА ЗАПРОСА ПО РЕЕСТРУ,НОМЕР ЗАПРОСА ПО РЕЕСТРУ,ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ,НОМЕР ПРЕДПИСАНИЯ ПО РЕЕСТРУ,ПРОВЕРКИ ГОСА ПО РАСКРЫТИЮ,ПРОВЕРКИ ГОСА ПО ЗАПРОСУ,ДАТА ПРОВЕДЕНИЯ ГОСА,ДАТА ЗАПРОСА ПО ГОСА,НОМЕР ЗАПРОСА ПО ГОСА,ПРОВЕРКА 1 ВЫПУСК,ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ,НОМЕР ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ,НРД,ПРОВЕРКИ НРД,ОАО на 22.06.2015,КОРП КОНТРОЛЬ,ПАО В СИЛУ ПРИЗНАКОВ СТ.30,ПАО В СИЛУ ПРИЗНАКОВ БЕЗ СТ. 30,ПАО В СИЛУ НАЗВАНИЯ СТ. 30,ПАО В СИЛУ НАЗВАНИЯ БЕЗ СТ. 30,НАО СО СТ. 30,НАО ОСУЩЕСТВИВШЕЕ (ОСУЩЕСТВЛЯЮЩЕЕ) ПУБЛИЧНОЕ РАЗМЕЩЕНИЕ ОБЛИГАЦИЙ ИЛИ ИНЫХ ЦЕННЫХ БУМАГ,НАО БЕЗ СТ. 30,ДАТА ОПРЕДЕЛЕНИЯ СТАТУСА,ОТКАЗ В РЕГИСТРАЦИИ ВЫПУСКА,ОСВОБОЖДЕНЫ ОТ РАСКРЫТИЯ ,ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ,НОМЕР РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ,ОТКАЗ В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ,ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ,НОМЕР ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ,ПРОВЕРКА РАСКРЫТИЯ,ДАТА ПРОВЕРКИ,ДАТА ЗАПРОСА ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ,НОМЕР ЗАПРОСА ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ,ДАТА ПРЕДПИСАНИЯ ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ,НОМЕР ПРЕДПИСАНИЯ ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ,ДАТА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ,НОМЕР ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ,ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ,НОМЕР ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ,ВЫВОД,РАСКРЫТИЕ,ДАТА ПРОТОКОЛА,НОМЕР ПРОТОКОЛА,СТАТЬЯ КОАП,ДАТА ПОСТАНОВЛЕНИЯ,НОМЕР ПОСТАНОВЛЕНИЯ,РЕЗУЛЬТАТ,РАЗМЕР ШТРАФА,АДМИНИСТРАТИВКА,ФНС ,ДАТА ПИСЬМА В ФНС,НОМЕР ПИСЬМА В ФНС,ИНФОРМАЦИЯ О ПОЛУЧЕНИИ ОТВЕТА ОТ ФНС,ВХ. НОМЕР ОТВЕТА,СОДЕРЖАНИЕ ОТВЕТА,ОТВЕТ ФНС ОБ АДРЕСЕ ,СВЕДЕНИЯ ОБ АДРЕСЕ НЕ ДОСТОВЕРНЫ,ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ,ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (НОМЕР ПИСЬМА),ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (ДАТА ПИСЬМА),ДАТА ВНЕСЕНИЯ ЗАПИСИ,ВЗАИМОДЕЙСТВИЕ С ГОС. ОРГАНАМИ) VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})'.format(dict['НАИМЕНОВАНИЕ'][i], dict['ИНН'][i], dict['ОГРН'][i], dict['КПП'][i],dict['ДАТА РЕГИСТРАЦИИ'][i], dict['ОПФ'][i], dict['КОД ЭМИТEHТA'][i],dict['УСТАВНЫЙ КАПИТАЛ'][i], dict['Количество лицевых счетов в реестре'][i],dict['Количество номинальных держателей в реестре'][i], dict['Сведения об открытии счета номинального держателя центрального депозитария'][i], dict['РЕГИОН'][i], dict['АДРЕС'][i], dict['ЕДИНОЛИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ ОРГАН'][i],dict['КОНТАКТНЫЕ ДАННЫЕ'][i], dict['СТАТУС'][i], dict['ДВИЖЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ'][i], dict['ДАТА ПОСЛЕДНЕЙ ОПЕРАЦИИ'][i], dict['ОТЧЕТНОСТЬ'][i],dict['ЗАДОЛЖЕННОСТЬ ПЕРЕД ФНС'][i], dict['КАРТОЧКА КОМПАНИИ'][i], dict['РЕГИСТРАТОР'][i], dict['РЕГИСТРАТОР'][i], dict['НАИМЕНОВАНИЕ РЕГИСТРАТОРА'][i],dict['ДАТА ПИСЬМА ПО РЕЕСТРУ'][i], dict['НОМЕР ПИСЬМА ПО РЕЕСТРУ'][i], dict['ДАТА ЗАПРОСА ПО РЕЕСТРУ'][i], dict['НОМЕР ЗАПРОСА ПО РЕЕСТРУ'][i], dict['ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ'][i],dict['НОМЕР ПРЕДПИСАНИЯ ПО РЕЕСТРУ'][i], dict['ПРОВЕРКИ ГОСА ПО РАСКРЫТИЮ'][i], dict['ПРОВЕРКИ ГОСА ПО ЗАПРОСУ'][i], dict['ДАТА ПРОВЕДЕНИЯ ГОСА'][i], dict['ДАТА ЗАПРОСА ПО ГОСА'][i],dict['НОМЕР ЗАПРОСА ПО ГОСА'][i], dict['ПРОВЕРКА 1 ВЫПУСК'][i], dict['ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ'][i], dict['НОМЕР ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ'][i], dict['НРД'][i],dict['ПРОВЕРКИ НРД'][i], dict['ОАО на 22.06.2015'][i], dict['КОРП КОНТРОЛЬ'][i], dict['ПАО В СИЛУ ПРИЗНАКОВ СТ.30'][i], dict['ПАО В СИЛУ ПРИЗНАКОВ БЕЗ СТ. 30'][i],dict['ПАО В СИЛУ НАЗВАНИЯ СТ. 30'][i], dict['ПАО В СИЛУ НАЗВАНИЯ БЕЗ СТ. 30'][i], dict['НАО СО СТ. 30'][i], dict['НАО ОСУЩЕСТВИВШЕЕ (ОСУЩЕСТВЛЯЮЩЕЕ) ПУБЛИЧНОЕ РАЗМЕЩЕНИЕ ОБЛИГАЦИЙ ИЛИ ИНЫХ ЦЕННЫХ БУМАГ'][i], dict['НАО БЕЗ СТ. 30'][i],dict['ДАТА ОПРЕДЕЛЕНИЯ СТАТУСА'][i], dict['ОТКАЗ В РЕГИСТРАЦИИ ВЫПУСКА'][i], dict[' ОСВОБОЖДЕНЫ ОТ РАСКРЫТИЯ'][i], dict['ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ'][i], dict['НОМЕР РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ'][i],dict['ОТКАЗ В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ'][i], dict['ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ'][i], dict['НОМЕР ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ'][i], dict['ПРОВЕРКА РАСКРЫТИЯ'][i], dict['ДАТА ПРОВЕРКИ'][i],dict['ДАТА ЗАПРОСА ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ'][i], dict['НОМЕР ЗАПРОСА ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ'][i], dict['ДАТА ПРЕДПИСАНИЯ ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ'][i], dict['НОМЕР ПРЕДПИСАНИЯ ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ'][i], dict['ДАТА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ'][i],dict['НОМЕР ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ'][i],dict['ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ'][i],dict['НОМЕР ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ'][i],dict['ВЫВОД'][i],dict['РАСКРЫТИЕ'][i], dict['ДАТА ПРОТОКОЛА'][i], dict['НОМЕР ПРОТОКОЛА'][i],dict['СТАТЬЯ КОАП'][i], dict['ДАТА ПОСТАНОВЛЕНИЯ'][i], dict['НОМЕР ПОСТАНОВЛЕНИЯ'][i], dict['РЕЗУЛЬТАТ'][i], dict['РАЗМЕР ШТРАФА'][i],dict['АДМИНИСТРАТИВКА'][i], dict['ФНС'][i],dict['ДАТА ПИСЬМА В ФНС'][i], dict['НОМЕР ПИСЬМА В ФНС'][i], dict['ИНФОРМАЦИЯ О ПОЛУЧЕНИИ ОТВЕТА ОТ ФНС'][i],dict['ВХ. НОМЕР ОТВЕТА'][i], dict['СОДЕРЖАНИЕ ОТВЕТА'][i], dict['ОТВЕТ ФНС ОБ АДРЕСЕ'][i], dict['СВЕДЕНИЯ ОБ АДРЕСЕ НЕ ДОСТОВЕРНЫ'][i], dict['ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ '][i],dict['ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (НОМЕР ПИСЬМА)'][i], dict['ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (ДАТА ПИСЬМА)'][i], dict['ДАТА ВНЕСЕНИЯ ЗАПИСИ'][i], dict['ВЗАИМОДЕЙСТВИЕ С ГОС. ОРГАНАМИ'][i]))
    cursor.close()

def delete_file():
    os.remove('update/DB.xlsm')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM app_document WHERE id >= (SELECT min(id) FROM app_document)")
    cursor.close()


    
 

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # xls = ExcelFile('update/DB.xlsm')
            # sh1 = xls.parse(xls.sheet_names[0])
            # sh2 = xls.parse(xls.sheet_names[1])
            # excel_dict1 = sh1.to_dict()
            # excel_dict2 = sh2.to_dict()

            # orgn_query_select('НЕТСАМИ')
            # custom_column_query_select('НЕТСАМИ')

      
            # delete_db_query()
            
            # update_db_query(excel_dict1)
            
            # custom_columns_query_insert('НЕТСАМИ')

            delete_file()


            return HttpResponseRedirect(reverse('list'))

        



    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    

    


    # Render list page with the documents and the form
    return render(
        request,
        'db_update.html',
        {'documents': documents, 'form': form, }
    )       







    
