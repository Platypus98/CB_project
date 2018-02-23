import os
from collections import namedtuple

import xlwt
from django.contrib import auth
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.db import connection
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from pandas import *

from .forms import *
from .models import *


# Create your views here.

def search(request):
    size_error = False
    data_error = False
    empty_error = False
    form = Data111Form(request.POST or None)
    limit = limitForm(request.POST or None)
    queryset = None
    context = {
        "queryset": queryset,
        "form": form,
        "limit": limit,
        "toomany": size_error,
        "nores": data_error
    }
    if request.method == 'POST':
        if form['naimenovanie'].value() == '' and form['inn'].value() == '' and form['ogrn'].value() == '' and form[
            'cod_emitenta'].value() == '':
            empty_error = True
        else:
            queryset = Data111.objects.all().filter(naimenovanie__icontains=form['naimenovanie'].value(),
                                                    inn__icontains=form['inn'].value(),
                                                    ogrn__icontains=form['ogrn'].value(),
                                                    cod_emitenta__icontains=form['cod_emitenta'].value())
        if queryset is not None and len(queryset) >= 5000:
            size_error = True
        if size_error or empty_error:
            queryset = None
        if not empty_error and not size_error:
            if len(queryset) == 0:
                data_error = True
        context = {
            "queryset": queryset,
            "form": form,
            "limit": limit,
            "toomany": size_error,
            "nores": data_error
        }
    return render(request, 'search.html', context)


def edit_kartochka(request, id):
    title = Data111.objects.get(id=id).naimenovanie
    obj = get_object_or_404(Data111, id=id)
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
    title = Data111.objects.get(id=id).naimenovanie
    obj = get_object_or_404(Data111, id=id)
    form = Data111Edit_Korp_KontrolForm(request.POST or None, instance=obj)
    if request.method == 'GET':
        if form['registrator1'].value() == 'НЕТ':
            noblock = True
        if form['netsami'].value() == 'САМИ В ЕГРЮЛ':
            sami = True
        if form['netsami'].value() is None:
            index = True
        if form['netsami'].value() == '---':
            index = True
        if form['netsami'].value() == 'НЕТ В ЕГРЮЛ':
            net = True
        if form['registrator1'].value() == 'НЕТ':
            naimenovanie_reg = False
        # if form['nomer_zaprosa_po_reestru'].value() is not None:
        #     otslezhivanie = True
        # if form['nomer_predpisaniya_po_reestru'].value() is not None:
        #     otslezhivanie1 = True

    if request.method == 'POST':
        if form['registrator1'].value() == 'НЕТ':
            noblock = True
        if form['netsami'].value() == 'САМИ В ЕГРЮЛ':
            sami = True
        if form['netsami'].value() is None:
            index = True
        if form['netsami'].value() == '---':
            index = True
        if form['netsami'].value() == 'НЕТ В ЕГРЮЛ':
            net = True
        if form['registrator1'].value() == 'НЕТ':
            naimenovanie_reg = False
            # if form['nomer_zaprosa_po_reestru'].value() is not None:
        #     otslezhivanie = True
        # if form['nomer_predpisaniya_po_reestru'].value() is not None:
        #     otslezhivanie1 = True
        if form.is_valid():
            form.save()

    context = {
        "title": title,
        "form": form,
        "id": id,
        "noblock": noblock,
        "sami": sami,
        "net": net,
        "naimenovanie_reg": naimenovanie_reg,
        "otslezhivanie": otslezhivanie,
        "index": index,
        "otslezhivanie1": otslezhivanie1,
    }

    return render(request, 'edit_korp_kontrol.html', context)


def edit_raskrytie(request, id):
    title = Data111.objects.get(id=id).naimenovanie
    obj = get_object_or_404(Data111, id=id)
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
    title = Data111.objects.get(id=id).naimenovanie
    obj = get_object_or_404(Data111, id=id)
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
    title = Data111.objects.get(id=id).naimenovanie
    obj = get_object_or_404(Data111, id=id)
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
    filter_list = []
    k = 0
    queryset = Data111.objects.all()

    columns_to_display = ['naimenovanie', 'inn', 'ogrn', 'kpp', 'data_registracii', 'opf', 'cod_emitenta',
                          'ustavnoy_capital',
                          'kolichestvo_licevyh_schetov_v_reestre', 'kolichestvo_nominalnyh_derzhateley_v_reestre',
                          'cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria', 'region',
                          'adres', 'edinolichny_ispolnitelny_organ', 'contactny_dannye', 'status',
                          'dvizhenie_denezhnyh_sredstv',
                          'data_posledney_operacii', 'otchetnost', 'zadolzhennost_pered_fns', 'registrator',
                          'naimenovanie_registratora', 'data_pisma_po_reestru', 'nomer_pisma_po_reestru',
                          'data_zaprosa_po_reestru', 'nomer_zaprosa_po_reestru', 'data_predpisanya_po_reestru',
                          'nomer_predpisaniya_po_reestru', 'data_provedeniya_gosa', 'data_zaprosa_po_gosa',
                          'proverky_gosa_po_zaprosu', 'proverky_gosa_po_raskritiyu',
                          'nomer_zaprosa_po_gosa', 'proverka_1_vipusk', 'data_predpisaniya_po_1_vypusku',
                          'nomer_predpisaniya_po_1_vypusku',
                          'nrd', 'proverki_nrd', 'oao_na_22_06_2015', 'pao_v_silu_priznakov_st30',
                          'pao_v_silu_priznakov_bez_st30', 'pao_v_silu_nazvaniya_st30',
                          'pao_v_silu_nazvaniya_bez_st30', 'nao_so_st30',
                          'nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag',
                          'nao_bez_st30', 'data_opredelenia_statusa', 'otkaz_v_registracii_vipuska',
                          'osvobozhdeny_ot_raskrytiya', 'data_resheniya_ob_osvobozhdenii',
                          'nomer_resheniya_ob_osvobozhdenii',
                          'otkaz_v_osvobozhdenii_ot_raskritiya', 'data_otkaza_v_osvobozhdenii_ot_raskritiya',
                          'nomer_otkaza_v_osvobozhdenii_ot_raskritiya',
                          'proverka_raskritiya', 'data_proverki', 'data_zaprosa_po_neraskritiyu_informacii',
                          'nomer_zaprosa_po_neraskritiyu_informacii', 'data_predpisaniya_po_neraskritiyu_informacii',
                          'nomer_predpisaniya_po_neraskritiyu_informacii',
                          'data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve',
                          'nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve',
                          'data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve',
                          'nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve', 'vivod', 'raskritie',
                          'data_protokola', 'nomer_protokola',
                          'statya_koap', 'data_postanovleniya', 'nomer_postanovleniya', 'resultat', 'razmer_shtrafa',
                          'administrativka', 'fns',
                          'data_pisma_v_fns', 'nomer_pisma_v_fns', 'informaciya_o_poluchenii_otveta_ot_fns',
                          'vh_nomer_otveta',
                          'soderzhanie_otveta', 'otvet_fns_ob_adrese', 'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove',
                          'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_nomer_pisma',
                          'vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_data_pisma',
                          'svedeniya_ob_adrese_ne_dostoverny', 'data_vneseniya_zapisi', 'vzaimodeystvie_s_gos_organami']

    form = Data111FormSelection(request.POST or None)
    form_filter_opf = Filter_opf(request.POST or None)
    form_filter_kolichestvo_schetov = Filter_kolichestvo_licevyh_schetov_v_reestre(request.POST or None)
    form_filter_region = Filter_region(request.POST or None)
    form_filter_status = Filter_status(request.POST or None)
    form_filter_dvizhenie_denezhnyh_sredstv = Filter_dvizhenie_denezhnyh_sredstv(request.POST or None)
    form_filter_otchetnost = Filter_otchetnost(request.POST or None)
    form_filter_zadolzhennost_pered_fns = Filter_zadolzhennost_pered_fns(request.POST or None)
    form_filter_registrator = Filter_registrator(request.POST or None)
    form_filter_proverka_gosa_po_raskratiu = Filter_proverka_gosa_po_raskratiu(request.POST or None)
    form_filter_proverky_gosa_po_zaprosu = Filter_proverky_gosa_po_zaprosu(request.POST or None)
    form_filter_nrd = Filter_nrd(request.POST or None)
    form_filter_proverki_nrd = Filter_proverky_nrd(request.POST or None)
    form_filter_oao_na_22062015 = Filter_oao_na_22062015(request.POST or None)
    form_filter_data_zaprosa_po_reestru = Filter_data_zaprosa_po_reestru(request.POST or None)

    context = {
        "form": form,
        "queryset": queryset,
        "form_filter_opf": form_filter_opf,
        "form_filter_kolichestvo_schetov": form_filter_kolichestvo_schetov,
        "form_filter_region": form_filter_region,
        "form_filter_status": form_filter_status,
        "form_filter_dvizhenie_denezhnyh_sredstv": form_filter_dvizhenie_denezhnyh_sredstv,
        "form_filter_otchetnost": form_filter_otchetnost,
        "form_filter_zadolzhennost_pered_fns": form_filter_zadolzhennost_pered_fns,
        "form_filter_registrator": form_filter_registrator,
        "form_filter_proverka_gosa_po_raskratiu": form_filter_proverka_gosa_po_raskratiu,
        "form_filter_proverky_gosa_po_zaprosu": form_filter_proverky_gosa_po_zaprosu,
        "form_filter_nrd": form_filter_nrd,
        "form_filter_proverki_nrd": form_filter_proverki_nrd,
        "form_filter_oao_na_22062015": form_filter_oao_na_22062015,
        "form_filter_data_zaprosa_po_reestru": form_filter_data_zaprosa_po_reestru,

    }

    # Отображение в браузере
    if request.method == 'POST':

        table_headers = map(lambda a: Data111._meta.get_field(a).help_text or a, columns_to_display)

        for i in form._meta.fields:
            if form[i].value():
                a.append(form[i].label)

        for i in form._meta.fields:
            if form[i].value():
                b.append(i)

        c = ['row.' + x for x in b]

        # Фильтры ОПФ
        if form['opf'].value():
            for i in ['ao', 'aozt', 'aoot', 'zao', 'nao', 'oao', 'pao']:
                if form_filter_opf[i].value():
                    filter_list.append(form_filter_opf[i].label)
            if filter_list == []:
                pass
            else:
                filter_ = Data111.objects.filter(opf__in=filter_list)
                k = 1

        filter_list = []
        # Фильтры количество лицевых счетов
        if form['kolichestvo_licevyh_schetov_v_reestre'].value():
            if k == 1:
                if form_filter_kolichestvo_schetov['bolshe_50'].value():
                    filter_ = filter_.filter(kolichestvo_licevyh_schetov_v_reestre__gte=50)
                elif form_filter_kolichestvo_schetov['menshe_50'].value():
                    filter_ = filter_.filter(kolichestvo_licevyh_schetov_v_reestre__lte=50)
            else:
                if form_filter_kolichestvo_schetov['bolshe_50'].value():
                    filter_ = Data111.objects.filter(kolichestvo_licevyh_schetov_v_reestre__gte=50)
                    k = 1
                elif form_filter_kolichestvo_schetov['menshe_50'].value():
                    filter_ = Data111.objects.filter(kolichestvo_licevyh_schetov_v_reestre__lte=2)
                    k = 1

        # Фильтры регион
        if form['region'].value():
            if k == 1:
                for i in ['moskva', 'moskovskaya']:
                    if form_filter_region[i].value():
                        filter_list.append(form_filter_region[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = filter_.filter(region__in=filter_list)
                filter_list = []
            else:
                for i in ['moskva', 'moskovskaya']:
                    if form_filter_region[i].value():
                        filter_list.append(form_filter_region[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = Data111.objects.filter(region__in=filter_list)
                    k = 1
                filter_list = []

        # Фильтры статус
        if form['status'].value():
            if k == 1:
                for i in ['bankrotstvo', 'deistvyushaya', 'nahoditca_v_processe_reorganizacii_v_forme_videlenya',
                          'nahoditca_v_processe_reorganizacii_v_forme_videlenya_osyshestvlyaemoe_odnovremenno_s_videleniem',
                          'nahoditca_v_processe_reorganizacii_v_forme_preobrazovanya',
                          'nahoditca_v_processe_reorganizacii_v_forme_prisoedinenya_k_drygomy_ul',
                          'nahoditca_v_processe_reorganizacii_v_forme_prisoedinenya_k_nemy_drygih_ul',
                          'nahoditca_v_processe_reorganizacii_v_forme_prisoedinenya_osychestvlyaemoy_odnovremenno_s_videleniem',
                          'nahoditca_v_processe_reorganizacii_v_forme_razdelenya_osychestvlyaemoy_odnovremenno_s_prisoedineniem',
                          'nahoditca_v_processe_reorganizacii_v_forme_sliyaniya',
                          'nahoditca_v_processe_reorganizacii_v_forme_razdelenya', 'nahoditca_v_stadii_likvidacii',
                          'prinyato_reshenie_o_predostoyashem_iskluchenii_nedeystvyushego_ul_iz_egrul']:
                    if form_filter_status[i].value():
                        filter_list.append(form_filter_status[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = filter_.filter(status__in=filter_list)
                filter_list = []
            else:
                for i in ['bankrotstvo', 'deistvyushaya', 'nahoditca_v_processe_reorganizacii_v_forme_videlenya',
                          'nahoditca_v_processe_reorganizacii_v_forme_videlenya_osyshestvlyaemoe_odnovremenno_s_videleniem',
                          'nahoditca_v_processe_reorganizacii_v_forme_preobrazovanya',
                          'nahoditca_v_processe_reorganizacii_v_forme_prisoedinenya_k_drygomy_ul',
                          'nahoditca_v_processe_reorganizacii_v_forme_prisoedinenya_k_nemy_drygih_ul',
                          'nahoditca_v_processe_reorganizacii_v_forme_prisoedinenya_osychestvlyaemoy_odnovremenno_s_videleniem',
                          'nahoditca_v_processe_reorganizacii_v_forme_razdelenya_osychestvlyaemoy_odnovremenno_s_prisoedineniem',
                          'nahoditca_v_processe_reorganizacii_v_forme_sliyaniya',
                          'nahoditca_v_processe_reorganizacii_v_forme_razdelenya', 'nahoditca_v_stadii_likvidacii',
                          'prinyato_reshenie_o_predostoyashem_iskluchenii_nedeystvyushego_ul_iz_egrul']:
                    if form_filter_status[i].value():
                        filter_list.append(form_filter_status[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = Data111.objects.filter(status__in=filter_list)
                    k = 1
                filter_list = []

        # Фильтры движение денежных средств
        if form['dvizhenie_denezhnyh_sredstv'].value():
            if k == 1:
                for i in ['da', 'net']:
                    if form_filter_dvizhenie_denezhnyh_sredstv[i].value():
                        filter_list.append(form_filter_dvizhenie_denezhnyh_sredstv[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = filter_.filter(dvizhenie_denezhnyh_sredstv__in=filter_list)
                filter_list = []
            else:
                for i in ['da', 'net']:
                    if form_filter_dvizhenie_denezhnyh_sredstv[i].value():
                        filter_list.append(form_filter_dvizhenie_denezhnyh_sredstv[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = Data111.objects.filter(dvizhenie_denezhnyh_sredstv__in=filter_list)
                    k = 1
                filter_list = []

        # Фильтры отчетность
        if form['otchetnost'].value():
            if k == 1:
                if form_filter_otchetnost['nepustaia'].value():
                    filter_ = filter_.exclude(otchetnost__exact="")
                elif form_filter_otchetnost['pustaia'].value():
                    filter_ = filter_.filter(otchetnost__exact="")
            else:
                if form_filter_otchetnost['nepustaia'].value():
                    filter_ = Data111.objects.exclude(otchetnost__exact="")
                    k = 1
                elif form_filter_otchetnost['pustaia'].value():
                    filter_ = Data111.objects.filter(otchetnost__exact="")
                    k = 1

        # Фильтры задолженность перед ФНС
        if form['zadolzhennost_pered_fns'].value():
            if k == 1:
                if form_filter_zadolzhennost_pered_fns['nepustaia'].value():
                    filter_ = filter_.exclude(zadolzhennost_pered_fns__exact="")
                elif form_filter_zadolzhennost_pered_fns['pustaia'].value():
                    filter_ = filter_.filter(zadolzhennost_pered_fns__exact="")
            else:
                if form_filter_zadolzhennost_pered_fns['nepustaia'].value():
                    filter_ = Data111.objects.exclude(zadolzhennost_pered_fns__exact="")
                    k = 1
                elif form_filter_zadolzhennost_pered_fns['pustaia'].value():
                    filter_ = Data111.objects.filter(zadolzhennost_pered_fns__exact="")
                    k = 1

        # Корп контроль
        # Фильтры дата запроса по реестру
        if form['data_zaprosa_po_reestru'].value():
            if k == 1:
                if form_filter_data_zaprosa_po_reestru["from_"] and form_filter_data_zaprosa_po_reestru['to']:
                    for i in range(Data111.objects.raw("SELECT count(id) FROM Data111")):
                        if (datetime.date(Data111.objects.all()[i].data_zaprosa_po_reestru) >= datetime.date(
                                form_filter_data_zaprosa_po_reestru["from_"])) and (
                                datetime.date(Data111.objects.all()[i].data_zaprosa_po_reestru) <= datetime.date(
                                form_filter_data_zaprosa_po_reestru["to"])):
                            pass
                        else:
                            filter_ = filter_.exclude(id=i)
            else:
                if form_filter_data_zaprosa_po_reestru["from_"] and form_filter_data_zaprosa_po_reestru['to']:
                    for i in range(Data111.objects.all().count()):
                        date_str = Data111.objects.all()[i].data_zaprosa_po_reestru
                        date_str_from = form_filter_data_zaprosa_po_reestru["from_"].value().split('-')
                        for k in range(len(date_str_from)):
                            if date_str_from[k][0] == "0":
                                date_str_from[k] = date_str_from[k][1]
                        date_str_to = form_filter_data_zaprosa_po_reestru["to"].value().split('-')
                        for k in range(len(date_str_to)):
                            if date_str_to[k][0] == "0":
                                date_str_to[k] = date_str_to[k][1]
                        if "\n" in date_str:
                            date_str = date_str.split("\n")
                            for i in date_str:
                                date_str_1 = i.split('.')
                                for j in range(len(date_str_1)):
                                    if date_str_1[j][0] == "0":
                                        date_str_1[j] = date_str_1[j][1]
                                if (datetime.date(int(date_str_1[2]), int(date_str_1[1]),
                                                  int(date_str_1[0])) > datetime.date(int(date_str_from[0]),
                                                                                      int(date_str_from[1]),
                                                                                      int(date_str_from[2]))) and (
                                        datetime.date(int(date_str_1[2]), int(date_str_1[1]),
                                                      int(date_str_1[0])) < datetime.date(int(date_str_to[0]),
                                                                                          int(date_str_to[1]),
                                                                                          int(date_str_to[2]))):
                                    check = 1

                                if i == 0:
                                    filter_ = Data111.objects.exclude(id=i)
                                else:
                                    filter_ = filter_.exclude(id=i)
                        else:
                            date_str = Data111.objects.all()[i].data_zaprosa_po_reestru.split('.')
                            if date_str == [""]:
                                if i == 0:
                                    filter_ = Data111.objects.exclude(id=i)
                                else:
                                    filter_ = filter_.exclude(id=i)
                                continue

                            if (datetime.date(int(date_str[2]), int(date_str[1]), int(date_str[0])) > datetime.date(
                                    int(date_str_from[0]), int(date_str_from[1]), int(date_str_from[2]))) and (
                                    datetime.date(int(date_str[2]), int(date_str[1]), int(date_str[0])) < datetime.date(
                                    int(date_str_to[0]), int(date_str_to[1]), int(date_str_to[2]))):
                                pass
                            else:
                                if i == 0:
                                    filter_ = Data111.objects.exclude(id=i)
                                else:
                                    filter_ = filter_.exclude(id=i)
                k = 1

        # Фильтры Регистратор
        if form['registrator'].value():
            if k == 1:
                for i in ["da", "net", "egrul", "chranenie_reestra"]:
                    if form_filter_registrator[i].value():
                        filter_list.append(form_filter_registrator[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = filter_.filter(registrator__in=filter_list)
                filter_list = []
            else:
                for i in ["da", "net", "egrul", "chranenie_reestra"]:
                    if form_filter_registrator[i].value():
                        filter_list.append(form_filter_registrator[i].label)
                if filter_list == []:
                    pass
                else:
                    filter_ = Data111.objects.filter(registrator__in=filter_list)
                    k = 1
                filter_list = []

        # Фильтры Проверка ГОСА по раскрытию
        if form["proverky_gosa_po_raskritiyu"].value():
            if k == 1:
                for i in ["maxi", "mini", "avr", "pusto"]:
                    if form_filter_proverka_gosa_po_raskratiu[i].value():
                        filter_list.append(form_filter_proverka_gosa_po_raskratiu[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = filter_.filter(proverky_gosa_po_raskritiyu__in=filter_list)
                filter_list = []
            else:
                for i in ["maxi", "mini", "avr", "pusto"]:
                    if form_filter_proverka_gosa_po_raskratiu[i].value():
                        filter_list.append(form_filter_proverka_gosa_po_raskratiu[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = Data111.objects.filter(proverky_gosa_po_raskritiyu__in=filter_list)
                    k = 1
                filter_list = []

        # Фильтры Проверка ГОСА по запросу
        if form["proverky_gosa_po_zaprosu"].value():
            if k == 1:
                for i in ["akt", "k_proverke", "pusto"]:
                    if form_filter_proverky_gosa_po_zaprosu[i].value():
                        filter_list.append(form_filter_proverky_gosa_po_zaprosu[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = filter_.filter(proverky_gosa_po_zaprosu__in=filter_list)
                filter_list = []
            else:
                for i in ["akt", "k_proverke", "pusto"]:
                    if form_filter_proverky_gosa_po_zaprosu[i].value():
                        filter_list.append(form_filter_proverky_gosa_po_zaprosu[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = Data111.objects.filter(proverky_gosa_po_zaprosu__in=filter_list)
                    k = 1
                filter_list = []

        # Фильтр НРД
        if form['nrd'].value():
            if k == 1:
                if form_filter_nrd['da'].value():
                    filter_ = filter_.filter(nrd__exact="ДА")
                elif form_filter_nrd['pusto'].value():
                    filter_ = filter_.filter(nrd__exact="")
            else:
                if form_filter_nrd['da'].value():
                    filter_ = Data111.objects.filter(nrd__exact="ДА")
                    k = 1
                elif form_filter_nrd['pusto'].value():
                    filter_ = Data111.objects.filter(nrd__exact="")
                    k = 1

        # Фильтры проверки НРД
        if form['proverki_nrd'].value():
            if k == 1:
                for i in ["da", "net_scheta", "pusto"]:
                    if form_filter_proverki_nrd[i].value():
                        filter_list.append(form_filter_proverki_nrd[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = filter_.filter(proverki_nrd__in=filter_list)
                filter_list = []
            else:
                for i in ["da", "net_scheta", "pusto"]:
                    if form_filter_proverki_nrd[i].value():
                        filter_list.append(form_filter_proverki_nrd[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = Data111.objects.filter(proverki_nrd__in=filter_list)
                    k = 1
                filter_list = []

        # Фильтры ОАО на 22.06.2015
        if form["oao_na_22_06_2015"].value():
            if k == 1:
                for i in ["da", "pusto"]:
                    if form_filter_oao_na_22062015[i].value():
                        filter_list.append(form_filter_oao_na_22062015[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = filter_.filter(oao_na_22_06_2015__in=filter_list)
                filter_list = []
            else:
                for i in ["da", "pusto"]:
                    if form_filter_oao_na_22062015[i].value():
                        filter_list.append(form_filter_oao_na_22062015[i].label)
                if filter_list == []:
                    pass
                else:
                    if "Пустая" in filter_list:
                        filter_list.remove("Пустая")
                        filter_list.append("")
                    filter_ = Data111.objects.filter(oao_na_22_06_2015__in=filter_list)
                    k = 1
                filter_list = []

        if k == 1:
            table_rows = filter_.values(*b)
        else:
            table_rows = Data111.objects.all().values(*b)

        # a.remove('Export to CSV')

        context = {
            "form": form,
            "a": a,
            "b": b,
            "c": c,
            "table_rows": table_rows,
            "table_headers": table_headers,
            "queryset": queryset,
            "form_filter_opf": form_filter_opf,
            "form_filter_kolichestvo_schetov": form_filter_kolichestvo_schetov,
            "form_filter_region": form_filter_region,
            "form_filter_status": form_filter_status,
            "form_filter_dvizhenie_denezhnyh_sredstv": form_filter_dvizhenie_denezhnyh_sredstv,
            "form_filter_otchetnost": form_filter_otchetnost,
            "form_filter_zadolzhennost_pered_fns": form_filter_zadolzhennost_pered_fns,
            "form_filter_registrator": form_filter_registrator,
            "form_filter_proverka_gosa_po_raskratiu": form_filter_proverka_gosa_po_raskratiu,
            "form_filter_proverky_gosa_po_zaprosu": form_filter_proverky_gosa_po_zaprosu,
            "form_filter_nrd": form_filter_nrd,
            "form_filter_proverki_nrd": form_filter_proverki_nrd,
            "form_filter_oao_na_22062015": form_filter_oao_na_22062015,
            "form_filter_data_zaprosa_po_reestru": form_filter_data_zaprosa_po_reestru,

        }

    # Экспорт в Excel
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

        if k == 1:
            queryset_1 = filter_.all()
        else:
            queryset_1 = Data111.objects.all()

        for obj in queryset_1:
            row_num += 1
            row = []
            for i in b:
                row.append(getattr(obj, i))

            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        ws.col(0).width = 20000
        wb.save(response)
        return response
    # Конец экспорта в Excel

    return render(request, 'selections.html', context)


def home(request):
    count = Data111.objects.all().count()

    current_user = request.user
    ident = current_user.id
    context = {"count": count, 'ident': ident}

    if ident is not None:
        context['name'] = current_user.username

    if request.method == 'POST':
        if ident is None:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                context['login_ok'] = True
                context['user_ok'] = user.first_name
                context['name'] = user.username
                return render(request, 'base.html', context)
            else:
                context['login_error'] = True
                return render(request, 'base.html', context)
        else:
            logout(request)
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, "base.html", context)


# ОБНОВА БД---------_________-------__________---------_______


def namedtuplefetchall(cursor):
    '''Делает хорошо итерируемый лист для
    работы с результами курсора'''
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def russkie_dates(dick):
    '''Русифицирует даты'''
    datelist = ['ДАТА РЕГИСТРАЦИИ', 'ДАТА ПОСЛЕДНЕЙ ОПЕРАЦИИ', 'ДАТА ПИСЬМА ПО РЕЕСТРУ', 'ДАТА ЗАПРОСА ПО РЕЕСТРУ',
                'ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ', 'ДАТА ПРОВЕДЕНИЯ ГОСА', 'ДАТА ЗАПРОСА ПО ГОСА', 'ДАТА ПРОВЕРКИ ГОСА',
                'ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ', 'ДАТА ОПРЕДЕЛЕНИЯ СТАТУСА', 'ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ',
                'ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', 'ДАТА ПРОВЕРКИ', 'ДАТА ЗАПРОСА ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ',
                'ДАТА ПРЕДПИСАНИЯ ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ',
                'ДАТА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ',
                'ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', 'ДАТА ЗАКЛЮЧЕНИЯ ЮРИСТАМ',
                'ДАТА ПРОТОКОЛА', 'ДАТА ПОСТАНОВЛЕНИЯ', 'ДАТА ПИСЬМА В ФНС',
                'ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (ДАТА ПИСЬМА)', 'ДАТА ВНЕСЕНИЯ ЗАПИСИ']

    for k in range(len(datelist)):
        for i in dick['{}'.format(datelist[k])].keys():
            if '00:00:00' in dick['{}'.format(datelist[k])][i]:
                year = dick['{}'.format(datelist[k])][i][:4]
                month = dick['{}'.format(datelist[k])][i][5:7]
                day = dick['{}'.format(datelist[k])][i][8:10]

                dick['{}'.format(datelist[k])][i] = '{}.{}.{}'.format(day, month, year)


def custom_column_query_select(column):
    '''Выбирает столбец, которого нет в эксельке и записывает в буффер'''
    cursor = connection.cursor()

    cursor.execute("SELECT {} FROM Data111".format(column))

    custom_column = namedtuplefetchall(cursor)

    cursor.close()

    return custom_column


def orgn_query_select(column):
    '''Выбирает соответствующий уникальный номер для буфферного столбца'''
    cursor = connection.cursor()

    cursor.execute("SELECT ОГРН FROM Data111 WHERE {} != 000".format(column))

    ogrn = namedtuplefetchall(cursor)

    cursor.close()

    return ogrn


def custom_columns_query_insert(column):
    '''Заполняет столбец базы буферными значениями'''

    custom = custom_column_query_select(column)

    ogrn = orgn_query_select(column)

    query = "UPDATE Data111 SET {} = %s WHERE ОГРН = %s;".format(column)

    l = []
    t = ()

    cursor = connection.cursor()

    cursor.execute("BEGIN TRANSACTION;")

    for i in range(len(ogrn)):
        l = []
        t = ()
        l.append(custom[i][0])
        l.append(ogrn[i][0])
        t = tuple(l)
        cursor.execute(query, t)

    cursor.execute("COMMIT;")

    cursor.close()


def delete_db_query():
    '''Стирает все значения БД'''
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Data111 WHERE id >= (SELECT min(id) FROM Data111)")

    cursor.close()


def update(dick, k):
    db_columns = ['ИНН', 'ОГРН', 'КПП', 'ДАТА_РЕГИСТРАЦИИ', 'ОПФ', 'КОД_ЭМИТEHТA', 'УСТАВНЫЙ_КАПИТАЛ',
                  'Количество_лицевых_счетов_в_реестре', 'Количество_номинальных_держателей_в_реестре',
                  'Сведения_об_открытии_счета_номинального_держателя_центрального_депозитария', 'РЕГИОН', 'АДРЕС',
                  'ЕДИНОЛИЧНЫЙ_ИСПОЛНИТЕЛЬНЫЙ_ОРГАН', 'КОНТАКТНЫЕ_ДАННЫЕ', 'СТАТУС', 'ДВИЖЕНИЕ_ДЕНЕЖНЫХ_СРЕДСТВ',
                  'ДАТА_ПОСЛЕДНЕЙ_ОПЕРАЦИИ', 'ОТЧЕТНОСТЬ', 'ЗАДОЛЖЕННОСТЬ_ПЕРЕД_ФНС', 'КАРТОЧКА_КОМПАНИИ',
                  'РЕГИСТРАТОР', 'НАИМЕНОВАНИЕ_РЕГИСТРАТОРА', 'ДАТА_ПИСЬМА_ПО_РЕЕСТРУ', 'НОМЕР_ПИСЬМА_ПО_РЕЕСТРУ',
                  'ДАТА_ЗАПРОСА_ПО_РЕЕСТРУ', 'НОМЕР_ЗАПРОСА_ПО_РЕЕСТРУ', 'ДАТА_ПРЕДПИСАНИЯ_ПО_РЕЕСТРУ',
                  'НОМЕР_ПРЕДПИСАНИЯ_ПО_РЕЕСТРУ', 'ПРОВЕРКИ_ГОСА_ПО_РАСКРЫТИЮ', 'ПРОВЕРКИ_ГОСА_ПО_ЗАПРОСУ',
                  'ДАТА_ПРОВЕДЕНИЯ_ГОСА', 'ДАТА_ЗАПРОСА_ПО_ГОСА', 'НОМЕР_ЗАПРОСА_ПО_ГОСА', 'ДАТА_ПРОВЕРКИ_ГОСА',
                  'ПРОВЕРКА_1_ВЫПУСК', 'ДАТА_ПРЕДПИСАНИЯ_ПО_1_ВЫПУСКУ', 'НОМЕР_ПРЕДПИСАНИЯ_ПО_1_ВЫПУСКУ', 'НРД',
                  'ПРОВЕРКИ_НРД', 'ОАО_на_22_06_2015', 'КОРП_КОНТРОЛЬ', 'ПАО_В_СИЛУ_ПРИЗНАКОВ_СТ_30',
                  'ПАО_В_СИЛУ_ПРИЗНАКОВ_БЕЗ_СТ_30', 'ПАО_В_СИЛУ_НАЗВАНИЯ_СТ_30', 'ПАО_В_СИЛУ_НАЗВАНИЯ_БЕЗ_СТ_30',
                  'НАО_СО_СТ_30',
                  'НАО_ОСУЩЕСТВИВШЕЕ_ОСУЩЕСТВЛЯЮЩЕЕ_ПУБЛИЧНОЕ_РАЗМЕЩЕНИЕ_ОБЛИГАЦИЙ_ИЛИ_ИНЫХ_ЦЕННЫХ_БУМАГ',
                  'НАО_БЕЗ_СТ_30', 'ДАТА_ОПРЕДЕЛЕНИЯ_СТАТУСА', 'ОТКАЗ_В_РЕГИСТРАЦИИ_ВЫПУСКА',
                  'ОСВОБОЖДЕНЫ_ОТ_РАСКРЫТИЯ', 'ДАТА_РЕШЕНИЯ_ОБ_ОСВОБОЖДЕНИИ', 'НОМЕР_РЕШЕНИЯ_ОБ_ОСВОБОЖДЕНИИ',
                  'ОТКАЗ_В_ОСВОБОЖДЕНИИ_ОТ_РАСКРЫТИЯ', 'ДАТА_ОТКАЗА_В_ОСВОБОЖДЕНИИ_ОТ_РАСКРЫТИЯ',
                  'НОМЕР_ОТКАЗА_В_ОСВОБОЖДЕНИИ_ОТ_РАСКРЫТИЯ', 'ПРОВЕРКА_РАСКРЫТИЯ', 'ДАТА_ПРОВЕРКИ',
                  'ДАТА_ЗАПРОСА_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ', 'НОМЕР_ЗАПРОСА_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ',
                  'ДАТА_ПРЕДПИСАНИЯ_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ', 'НОМЕР_ПРЕДПИСАНИЯ_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ',
                  'ДАТА_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ',
                  'НОМЕР_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ',
                  'ДАТА_ОТВЕТА_НА_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ',
                  'НОМЕР_ОТВЕТА_НА_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ', 'ВЫВОД', 'РАСКРЫТИЕ',
                  'ДАТА_ЗАКЛЮЧЕНИЯ_ЮРИСТАМ', 'НОМЕР_ЗАКЛЮЧЕНИЯ_ЮРИСТАМ', 'ДАТА_ПРОТОКОЛА', 'НОМЕР_ПРОТОКОЛА',
                  'СТАТЬЯ_КОАП', 'ДАТА_ПОСТАНОВЛЕНИЯ', 'НОМЕР_ПОСТАНОВЛЕНИЯ', 'РЕЗУЛЬТАТ', 'РАЗМЕР_ШТРАФА',
                  'АДМИНИСТРАТИВКА', 'ФНС', 'ДАТА_ПИСЬМА_В_ФНС', 'НОМЕР_ПИСЬМА_В_ФНС',
                  'ИНФОРМАЦИЯ_О_ПОЛУЧЕНИИ_ОТВЕТА_ОТ_ФНС', 'ВХ_НОМЕР_ОТВЕТА', 'СОДЕРЖАНИЕ_ОТВЕТА', 'ОТВЕТ_ФНС_ОБ_АДРЕСЕ',
                  'СВЕДЕНИЯ_ОБ_АДРЕСЕ_НЕ_ДОСТОВЕРНЫ', 'ВЗАИМОДЕЙСТВИЕ_С_ФНС_НА_ЕЖЕКВАРТАЛЬНОЙ_ОСНОВЕ',
                  'ВЗАИМОДЕЙСТВИЕ_С_ФНС_НА_ЕЖЕКВАРТАЛЬНОЙ_ОСНОВЕ_НОМЕР_ПИСЬМА',
                  'ВЗАИМОДЕЙСТВИЕ_С_ФНС_НА_ЕЖЕКВАРТАЛЬНОЙ_ОСНОВЕ_ДАТА_ПИСЬМА', 'ДАТА_ВНЕСЕНИЯ_ЗАПИСИ',
                  'ВЗАИМОДЕЙСТВИЕ_С_ГОС_ОРГАНАМИ']
    excel_columns = []
    for I in dick.keys():
        excel_columns.append(I)
    excel_columns.remove('НАИМЕНОВАНИЕ')
    # excel_columns = list(dick.keys())

    cursor = connection.cursor()
    query = "UPDATE Data111 SET {} = %s WHERE id = %s;".format(db_columns[k])
    l = []
    t = ()

    cursor.execute("BEGIN TRANSACTION;")

    for i in dick['ОГРН'].keys():
        l = []
        t = ()
        l.append(dick[excel_columns[k]][i])
        l.append(i + 1)
        t = tuple(l)
        cursor.execute(query, t)

    cursor.execute("COMMIT;")

    cursor.close()


def delete_file():
    '''Удаляет файл эксель с БД из media'''
    os.remove('update/DB.xlsm')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM app_document WHERE id >= (SELECT min(id) FROM app_document)")
    cursor.close()


def list(request):
    # Загрузчик файла эксель
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            xls = ExcelFile('update/DB.xlsm')

            sh1 = xls.parse(xls.sheet_names[0], converters={'НАИМЕНОВАНИЕ': str, 'ИНН': str, 'ОГРН': str, 'КПП': str,
                                                            'ДАТА РЕГИСТРАЦИИ': str, 'ОПФ': str, 'КОД ЭМИТEHТA': str,
                                                            'УСТАВНЫЙ КАПИТАЛ': str,
                                                            'Количество лицевых счетов в реестре': str,
                                                            'Количество номинальных держателей в реестре': str,
                                                            'Сведения об открытии счета номинального держателя центрального депозитария': str,
                                                            'РЕГИОН': str, 'АДРЕС': str,
                                                            'ЕДИНОЛИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ ОРГАН': str,
                                                            'КОНТАКТНЫЕ ДАННЫЕ': str, 'СТАТУС': str,
                                                            'ДВИЖЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ': str,
                                                            'ДАТА ПОСЛЕДНЕЙ ОПЕРАЦИИ': str, 'ОТЧЕТНОСТЬ': str,
                                                            'ЗАДОЛЖЕННОСТЬ ПЕРЕД ФНС': str, 'КАРТОЧКА КОМПАНИИ': str,
                                                            'РЕГИСТРАТОР': str, 'НАИМЕНОВАНИЕ РЕГИСТРАТОРА': str,
                                                            'ДАТА ПИСЬМА ПО РЕЕСТРУ': str,
                                                            'НОМЕР ПИСЬМА ПО РЕЕСТРУ': str,
                                                            'ДАТА ЗАПРОСА ПО РЕЕСТРУ': str,
                                                            'НОМЕР ЗАПРОСА ПО РЕЕСТРУ': str,
                                                            'ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ': str,
                                                            'НОМЕР ПРЕДПИСАНИЯ ПО РЕЕСТРУ': str,
                                                            'ПРОВЕРКИ ГОСА ПО РАСКРЫТИЮ': str,
                                                            'ПРОВЕРКИ ГОСА ПО ЗАПРОСУ': str,
                                                            'ДАТА ПРОВЕДЕНИЯ ГОСА': str, 'ДАТА ЗАПРОСА ПО ГОСА': str,
                                                            'НОМЕР ЗАПРОСА ПО ГОСА': str, 'ДАТА ПРОВЕРКИ ГОСА': str,
                                                            'ПРОВЕРКА 1 ВЫПУСК': str,
                                                            'ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ': str,
                                                            'НОМЕР ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ': str, 'НРД': str,
                                                            'ПРОВЕРКИ НРД': str, 'ОАО на 22.06.2015': str,
                                                            'КОРП КОНТРОЛЬ': str, 'ПАО В СИЛУ ПРИЗНАКОВ СТ.30': str,
                                                            'ПАО В СИЛУ ПРИЗНАКОВ БЕЗ СТ. 30': str,
                                                            'ПАО В СИЛУ НАЗВАНИЯ СТ. 30': str,
                                                            'ПАО В СИЛУ НАЗВАНИЯ БЕЗ СТ. 30': str, 'НАО СО СТ. 30': str,
                                                            'НАО ОСУЩЕСТВИВШЕЕ (ОСУЩЕСТВЛЯЮЩЕЕ) ПУБЛИЧНОЕ РАЗМЕЩЕНИЕ ОБЛИГАЦИЙ ИЛИ ИНЫХ ЦЕННЫХ БУМАГ': str,
                                                            'НАО БЕЗ СТ. 30': str, 'ДАТА ОПРЕДЕЛЕНИЯ СТАТУСА': str,
                                                            'ОТКАЗ В РЕГИСТРАЦИИ ВЫПУСКА': str,
                                                            'ОСВОБОЖДЕНЫ ОТ РАСКРЫТИЯ': str,
                                                            'ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ': str,
                                                            'НОМЕР РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ': str,
                                                            'ОТКАЗ В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ': str,
                                                            'ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ': str,
                                                            'НОМЕР ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ': str,
                                                            'ПРОВЕРКА РАСКРЫТИЯ': str, 'ДАТА ПРОВЕРКИ': str,
                                                            'ДАТА ЗАПРОСА ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ': str,
                                                            'НОМЕР ЗАПРОСА ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ': str,
                                                            'ДАТА ПРЕДПИСАНИЯ ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ': str,
                                                            'НОМЕР ПРЕДПИСАНИЯ ПО НЕ РАСКРЫТИЮ ИНФОРМАЦИИ': str,
                                                            'ДАТА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ': str,
                                                            'НОМЕР ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ': str,
                                                            'ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ': str,
                                                            'НОМЕР ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ': str,
                                                            'ВЫВОД': str, 'РАСКРЫТИЕ': str,
                                                            'ДАТА ЗАКЛЮЧЕНИЯ ЮРИСТАМ': str,
                                                            'НОМЕР ЗАКЛЮЧЕНИЯ ЮРИСТАМ': str, 'ДАТА ПРОТОКОЛА': str,
                                                            'НОМЕР ПРОТОКОЛА': str, 'СТАТЬЯ КОАП': str,
                                                            'ДАТА ПОСТАНОВЛЕНИЯ': str, 'НОМЕР ПОСТАНОВЛЕНИЯ': str,
                                                            'РЕЗУЛЬТАТ': str, 'РАЗМЕР ШТРАФА': str,
                                                            'АДМИНИСТРАТИВКА': str, 'ФНС': str,
                                                            'ДАТА ПИСЬМА В ФНС': str, 'НОМЕР ПИСЬМА В ФНС': str,
                                                            'ИНФОРМАЦИЯ О ПОЛУЧЕНИИ ОТВЕТА ОТ ФНС': str,
                                                            'ВХ. НОМЕР ОТВЕТА': str, 'СОДЕРЖАНИЕ ОТВЕТА': str,
                                                            'ОТВЕТ ФНС ОБ АДРЕСЕ': str,
                                                            'СВЕДЕНИЯ ОБ АДРЕСЕ НЕ ДОСТОВЕРНЫ': str,
                                                            'ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ': str,
                                                            'ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (НОМЕР ПИСЬМА)': str,
                                                            'ВЗАИМОДЕЙСТВИЕ С ФНС НА ЕЖЕКВАРТАЛЬНОЙ ОСНОВЕ (ДАТА ПИСЬМА)': str,
                                                            'ДАТА ВНЕСЕНИЯ ЗАПИСИ': str,
                                                            'ВЗАИМОДЕЙСТВИЕ С ГОС. ОРГАНАМИ': str})
            sh1 = sh1.fillna('')

            sh2 = xls.parse(xls.sheet_names[1])

            excel_dict1 = sh1.to_dict()

            russkie_dates(excel_dict1)

            # orgn_query_select('НЕТСАМИ')
            # custom_column_query_select('НЕТСАМИ')

            delete_db_query()

            cursor = connection.cursor()

            query = "INSERT INTO Data111 (НАИМЕНОВАНИЕ) VALUES (%s);"
            l = []
            t = ()

            cursor.execute("BEGIN TRANSACTION;")

            for i in excel_dict1['ОГРН'].keys():
                l = []
                t = ()
                l.append(excel_dict1['НАИМЕНОВАНИЕ'][i])
                t = tuple(l)
                cursor.execute(query, t)

            cursor.execute("COMMIT;")

            cursor.close()

            for k in range(91):
                update(excel_dict1, k)

            cursor = connection.cursor()
            cursor.execute("UPDATE Data111 SET РЕГИСТРАТОР1 = РЕГИСТРАТОР")
            cursor.close()

            # custom_columns_query_insert('НЕТСАМИ')

            delete_file()

            # Обновляет страницу
            return HttpResponseRedirect(reverse('list'))



    else:
        form = DocumentForm()  # Пустая форма

    return render(
        request,
        'db_update.html',
        {'form': form, }
    )
