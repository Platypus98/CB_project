from django.shortcuts import render, redirect

import json

from django.shortcuts import get_object_or_404
from django.contrib import messages

from .forms import *

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
         #  queryset = Data111.objects.all().filter(naimenovanie__icontains = form['naimenovanie'].value(), inn__icontains = form['inn'].value(), ogrn__icontains = form['ogrn'].value(), cod_emitenta__icontains = form['cod_emitenta'].value() )
            queryset = Data111.objects.filter(naimenovanie__icontains = form['naimenovanie'].value(), inn__icontains = form['inn'].value(), ogrn__icontains = form['ogrn'].value())
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
  title = Data111.objects.get(id = id).naimenovanie
  obj = get_object_or_404(Data111, id = id)
  form = Data111Edit_Korp_KontrolForm(request.POST or None, instance=obj)
  if request.method == 'POST':
    form.save()
  context = {
    "title": title,
    "form": form,
    "id": id,
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
    columns_to_display = ['naimenovanie', 'inn', 'ogrn','data_registracii','opf','cod_emitenta','ustavnoy_capital', 
                  'kolichestvo_licevyh_schetov_v_reestre', 'kolichestvo_nominalnyh_derzhateley_v_reestre', 
                  'cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria', 'region', 
                  'adres', 'edinolichny_ispolnitelny_organ', 'contactny_dannye', 'status', 'dvizhenie_denezhnyh_sredstv', 
                  'otchetnost', 'zadolzhennost_pered_fns', 'registrator', 'data_pisma_po_reestru', 'nomer_pisma_po_reestru', 
                  'data_zaprosa_po_reestru', 'nomer_zaprosa_po_reestru', 'data_predpisanya_po_reestru', 
                  'nomer_predpisaniya_po_reestru', 'data_provedeniya_gosa', 'data_zaprosa_po_gosa', 
                  'nomer_zaprosa_po_gosa','data_predpisaniya_po_1_vypusku','nomer_predpisaniya_po_1_vypusku', 
                  'nrd', 'oao_na_22_06_2015', 'pao_v_silu_priznakov', 'pao_v_silu_nazvaniya', 
                  'nao_obyazannoe_raskryvat_informaciyu_v_sootvetstvii_so_st_30_fz_o_pcb', 
                  'nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag', 
                  'nao', 'osvobozhdeny_ot_raskrytiya', 'data_resheniya_ob_osvobozhdenii','nomer_resheniya_ob_osvobozhdenii',
                  'otkaz_v_osvobozhdenii_ot_raskritiya','data_otkaza_v_osvobozhdenii_ot_raskritiya', 'nomer_otkaza_v_osvobozhdenii_ot_raskritiya', 
                  'proverka_raskritiya', 'data_proverki', 'data_zaprosa_po_neraskritiyu_informacii', 
                  'nomer_zaprosa_po_neraskritiyu_informacii', 'data_predpisaniya_po_neraskritiyu_informacii', 
                  'nomer_predpisaniya_po_neraskritiyu_informacii', 'data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve',
                  'nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve', 
                  'nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve','vivod', 'raskritie', 'data_protokola', 'nomer_protokola', 
                  'statya_koap','data_postanovleniya','nomer_postanovleniya', 'resultat', 'razmer_shtrafa','administrativka','fns', 
                  'data_pisma_v_fns', 'nomer_pisma_v_fns', 'informaciya_o_poluchenii_otveta_ot_fns', 'vh_nomer_otveta', 
                  'svedeniya_ob_adrese_ne_dostoverny', 'data_vneseniya_zapisi', 'vzaimodeystvie_s_gos_organami']

    form = Data111FormSelection(request.POST or None)
    context = {
    "form": form,
    }



    if request.method == 'POST':

        table_headers = map(lambda a: Data111._meta.get_field(a).help_text or a, columns_to_display)

        for i in form._meta.fields:      
            if form[i].value(): 
               a.append(form[i].label)

        for i in form._meta.fields:      
            if form[i].value(): 
               b.append(i)

        table_rows = Data111.objects.all().values(*b)

        context = {
        "form": form,
            "a": a,
            "b":b,
            "table_rows": table_rows,
            "table_headers": table_headers,
      }
      
    return render(request, 'selections.html', context)


def home(request):
  title = 'Добро пожаловать'
  context = {
    "title": title,
  }
  return render(request, "base.html",context)