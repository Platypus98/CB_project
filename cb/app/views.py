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
            if form['netsami'].value() == 'НЕТ В ЕГРЮЛ':
                 net = True
            if form['registrator1'].value() == 'НЕТ':
                 naimenovanie_reg = False
            if form['nomer_zaprosa_po_reestru'].value() is not None:
                 otslezhivanie = True
            if form['nomer_predpisaniya_po_reestru'].value() is not None:
                 otslezhivanie1 = True      

    if request.method == 'POST': 
            if form['registrator1'].value() == 'НЕТ':
                 noblock = True
            if form['netsami'].value() == 'САМИ В ЕГРЮЛ':
                 sami = True 
            if form['netsami'].value()  is None:
                 index = True       
            if form['netsami'].value() == 'НЕТ В ЕГРЮЛ':
                 net = True 
            if form['registrator1'].value() == 'НЕТ':
                 naimenovanie_reg = False 
            if form['nomer_zaprosa_po_reestru'].value() is not None:
                 otslezhivanie = True
            if form['nomer_predpisaniya_po_reestru'].value() is not None:
                 otslezhivanie1 = True                  
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
				#	for i in ['ao','aozt', 'aoot', 'zao', 'nao', 'oao', 'pao']:
				#		if form_filter_opf[i].value():
				#			table_rows = Data111.objects.filter(opf__exact=form_filter_opf[i].label)
				
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
	title = 'Добро пожаловать'
	context = {
		"title": title,
	}
	return render(request, "base.html",context)
