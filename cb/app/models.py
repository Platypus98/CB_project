#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

import os
from uuid import uuid4

import datetime

now = datetime.datetime.now()


class AuthGroup(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	name = models.CharField(unique=True, max_length=80)

	class Meta:
		managed = False
		db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
	permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_group_permissions'
		unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
	codename = models.CharField(max_length=100)
	name = models.CharField(max_length=255)

	class Meta:
		managed = False
		db_table = 'auth_permission'
		unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	password = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True, null=True)
	is_superuser = models.BooleanField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=254)
	is_staff = models.BooleanField()
	is_active = models.BooleanField()
	date_joined = models.DateTimeField()
	username = models.CharField(unique=True, max_length=150)

	class Meta:
		managed = False
		db_table = 'auth_user'


class AuthUserGroups(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_user_groups'
		unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

	class Meta:
		managed = False
		db_table = 'auth_user_user_permissions'
		unique_together = (('user', 'permission'),)



class Data111(models.Model):

	registrator_choices = (
		('ДА', 'Да'),
		('НЕТ', 'Нет'),
		('ЕГРЮЛ', 'ЕГРЮЛ'),
		('Хранение реестра', 'Хранение'),
	)


	id = models.IntegerField(unique=True, blank=True, primary_key=True)	
	naimenovanie = models.CharField(db_column='НАИМЕНОВАНИЕ', blank=True, null=True, max_length=1000, default=None)  
	inn = models.CharField(db_column='ИНН', blank=True, null=True, default=None,max_length=30)  
	ogrn = models.CharField(db_column='ОГРН', blank=True, null=True, default=None, max_length=100) 
	kpp = models.CharField(db_column='КПП', blank=True, null=True,max_length=100)  
	data_registracii = models.CharField(db_column='ДАТА_РЕГИСТРАЦИИ', blank=True, null=True, default=None, max_length=100)  
	opf = models.CharField(db_column='ОПФ', blank=True, null=True, default=None, max_length=100)  
	cod_emitenta = models.CharField(db_column='КОД_ЭМИТEHТA', blank=True, null=True, default=None, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	ustavnoy_capital = models.CharField(db_column='УСТАВНЫЙ_КАПИТАЛ', blank=True, null=True, default=None,max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	kolichestvo_licevyh_schetov_v_reestre = models.IntegerField(db_column='Количество_лицевых_счетов_в_реестре', blank=True, null=True, default=None,max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	kolichestvo_nominalnyh_derzhateley_v_reestre = models.CharField(db_column='Количество_номинальных_держателей_в_реестре', blank=True, null=True, default=None,max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria = models.CharField(db_column='Сведения_об_открытии_счета_номинального_держателя_центрального_депозитария', blank=True, null=True, default=None,max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	region = models.CharField(db_column='РЕГИОН', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase.
	adres = models.CharField(db_column='АДРЕС', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase.
	edinolichny_ispolnitelny_organ = models.CharField(db_column='ЕДИНОЛИЧНЫЙ_ИСПОЛНИТЕЛЬНЫЙ_ОРГАН', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	contactny_dannye = models.CharField(db_column='КОНТАКТНЫЕ_ДАННЫЕ', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	status = models.CharField(db_column='СТАТУС', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase.
	dvizhenie_denezhnyh_sredstv = models.CharField(db_column='ДВИЖЕНИЕ_ДЕНЕЖНЫХ_СРЕДСТВ', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_posledney_operacii = models.CharField(db_column='ДАТА_ПОСЛЕДНЕЙ_ОПЕРАЦИИ', blank=True, null= True, max_length= 1000)
	otchetnost = models.CharField(db_column='ОТЧЕТНОСТЬ', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase.
	zadolzhennost_pered_fns = models.CharField(db_column='ЗАДОЛЖЕННОСТЬ_ПЕРЕД_ФНС', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	kartochka_kompanii = models.CharField(db_column='КАРТОЧКА_КОМПАНИИ', blank=True, null=True, default=None, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	
	registrator1 = models.CharField(db_column='РЕГИСТРАТОР1', blank= False, null=False, max_length=20, default='ДА')  # Field name made lowercase.

	registrator = models.CharField(db_column='РЕГИСТРАТОР', blank=True, null=False, max_length=20)  # Field name made lowercase.

	netsami = models.CharField(db_column='НЕТСАМИ', blank=True, null=False, max_length=1000, default ='---')  # Field name made lowercase.



	naimenovanie_registratora = models.CharField(db_column='НАИМЕНОВАНИЕ_РЕГИСТРАТОРА', blank=True, max_length=1000, null=True)
	data_pisma_po_reestru = models.CharField(db_column='ДАТА_ПИСЬМА_ПО_РЕЕСТРУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_pisma_po_reestru = models.CharField(db_column='НОМЕР_ПИСЬМА_ПО_РЕЕСТРУ',blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_po_reestru = models.CharField(db_column='ДАТА_ЗАПРОСА_ПО_РЕЕСТРУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_po_reestru = models.CharField(db_column='НОМЕР_ЗАПРОСА_ПО_РЕЕСТРУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_predpisanya_po_reestru = models.CharField(db_column='ДАТА_ПРЕДПИСАНИЯ_ПО_РЕЕСТРУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_predpisaniya_po_reestru = models.CharField(db_column='НОМЕР_ПРЕДПИСАНИЯ_ПО_РЕЕСТРУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	proverky_gosa_po_raskritiyu = models.CharField(db_column='ПРОВЕРКИ_ГОСА_ПО_РАСКРЫТИЮ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	proverky_gosa_po_zaprosu = models.CharField(db_column='ПРОВЕРКИ_ГОСА_ПО_ЗАПРОСУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_provedeniya_gosa = models.CharField(db_column='ДАТА_ПРОВЕДЕНИЯ_ГОСА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_po_gosa = models.CharField(db_column='ДАТА_ЗАПРОСА_ПО_ГОСА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_po_gosa = models.CharField(db_column='НОМЕР_ЗАПРОСА_ПО_ГОСА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	
	###
	data_proverki_gosa = models.CharField(db_column='ДАТА_ПРОВЕРКИ_ГОСА', blank=True, null=True, max_length=1000)
	
	proverka_1_vipusk = models.CharField(db_column='ПРОВЕРКА_1_ВЫПУСК', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.  
	data_predpisaniya_po_1_vypusku = models.CharField(db_column='ДАТА_ПРЕДПИСАНИЯ_ПО_1_ВЫПУСКУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_predpisaniya_po_1_vypusku = models.CharField(db_column='НОМЕР_ПРЕДПИСАНИЯ_ПО_1_ВЫПУСКУ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nrd = models.CharField(db_column='НРД', blank=True, null=True, max_length=1000)  # Field name made lowercase.
	proverki_nrd = models.CharField(db_column='ПРОВЕРКИ_НРД', blank=True, null=True, max_length=1000)
	oao_na_22_06_2015 = models.CharField(db_column='ОАО_на_22_06_2015', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	korp_kontrol = models.CharField(db_column='КОРП_КОНТРОЛЬ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	
	pao_v_silu_priznakov_st30 = models.CharField(db_column='ПАО_В_СИЛУ_ПРИЗНАКОВ_СТ_30', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	pao_v_silu_priznakov_bez_st30 = models.CharField(db_column='ПАО_В_СИЛУ_ПРИЗНАКОВ_БЕЗ_СТ_30', blank=True, null=True, max_length=1000)
	pao_v_silu_nazvaniya_st30 = models.CharField(db_column='ПАО_В_СИЛУ_НАЗВАНИЯ_СТ_30', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	pao_v_silu_nazvaniya_bez_st30 = models.CharField(db_column='ПАО_В_СИЛУ_НАЗВАНИЯ_БЕЗ_СТ_30', blank=True, null=True, max_length=1000) 
	nao_so_st30 = models.CharField(db_column='НАО_СО_СТ_30', blank=True, null=True, max_length=1000) 
	nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag = models.CharField(db_column='НАО_ОСУЩЕСТВИВШЕЕ_ОСУЩЕСТВЛЯЮЩЕЕ_ПУБЛИЧНОЕ_РАЗМЕЩЕНИЕ_ОБЛИГАЦИЙ_ИЛИ_ИНЫХ_ЦЕННЫХ_БУМАГ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
	nao_bez_st30 = models.CharField(db_column='НАО_БЕЗ_СТ_30', blank=True, null=True, max_length=1000)  # Field name made lowercase.    
	data_opredelenia_statusa = models.CharField(db_column='ДАТА_ОПРЕДЕЛЕНИЯ_СТАТУСА', blank=True, null=True, max_length=1000)
	otkaz_v_registracii_vipuska = models.CharField(db_column='ОТКАЗ_В_РЕГИСТРАЦИИ_ВЫПУСКА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	osvobozhdeny_ot_raskrytiya = models.CharField(db_column='ОСВОБОЖДЕНЫ_ОТ_РАСКРЫТИЯ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_resheniya_ob_osvobozhdenii = models.CharField(db_column='ДАТА_РЕШЕНИЯ_ОБ_ОСВОБОЖДЕНИИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_resheniya_ob_osvobozhdenii = models.CharField(db_column='НОМЕР_РЕШЕНИЯ_ОБ_ОСВОБОЖДЕНИИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	otkaz_v_osvobozhdenii_ot_raskritiya = models.CharField(db_column='ОТКАЗ_В_ОСВОБОЖДЕНИИ_ОТ_РАСКРЫТИЯ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_otkaza_v_osvobozhdenii_ot_raskritiya = models.CharField(db_column='ДАТА_ОТКАЗА_В_ОСВОБОЖДЕНИИ_ОТ_РАСКРЫТИЯ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_otkaza_v_osvobozhdenii_ot_raskritiya = models.CharField(db_column='НОМЕР_ОТКАЗА_В_ОСВОБОЖДЕНИИ_ОТ_РАСКРЫТИЯ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	proverka_raskritiya = models.CharField(db_column='ПРОВЕРКА_РАСКРЫТИЯ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_proverki = models.CharField(db_column='ДАТА_ПРОВЕРКИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_po_neraskritiyu_informacii = models.CharField(db_column='ДАТА_ЗАПРОСА_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_po_neraskritiyu_informacii = models.CharField(db_column='НОМЕР_ЗАПРОСА_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_predpisaniya_po_neraskritiyu_informacii = models.CharField(db_column='ДАТА_ПРЕДПИСАНИЯ_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_predpisaniya_po_neraskritiyu_informacii = models.CharField(db_column='НОМЕР_ПРЕДПИСАНИЯ_ПО_НЕ_РАСКРЫТИЮ_ИНФОРМАЦИИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.CharField(db_column='ДАТА_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.CharField(db_column='НОМЕР_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.CharField(db_column='ДАТА_ОТВЕТА_НА_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.CharField(db_column='НОМЕР_ОТВЕТА_НА_ЗАПРОСА_О_РЕЗУЛЬТАТАХ_ПРОВЕДЕНИЯ_ТОРГОВ_В_ОБЩЕСТВЕ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	vivod = models.CharField(db_column='ВЫВОД', blank=True, null=True, max_length=1000)  # Field name made lowercase.
	raskritie = models.CharField(db_column='РАСКРЫТИЕ', blank=True, null=True, max_length=1000)  # Field name made lowercase.
	
	###
	data_zaclucheniya_uristam = models.CharField(db_column='ДАТА_ЗАКЛЮЧЕНИЯ_ЮРИСТАМ', blank=True, null=True, max_length=1000)
	nomer_zaclucheniya_uristam = models.CharField(db_column='НОМЕР_ЗАКЛЮЧЕНИЯ_ЮРИСТАМ', blank=True, null=True, max_length=1000)


	data_protokola = models.CharField(db_column='ДАТА_ПРОТОКОЛА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_protokola = models.CharField(db_column='НОМЕР_ПРОТОКОЛА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	statya_koap = models.CharField(db_column='СТАТЬЯ_КОАП', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_postanovleniya = models.CharField(db_column='ДАТА_ПОСТАНОВЛЕНИЯ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_postanovleniya = models.CharField(db_column='НОМЕР_ПОСТАНОВЛЕНИЯ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	resultat = models.CharField(db_column='РЕЗУЛЬТАТ', blank=True, null=True, max_length=1000)  # Field name made lowercase.
	razmer_shtrafa = models.CharField(db_column='РАЗМЕР_ШТРАФА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	administrativka = models.CharField(db_column='АДМИНИСТРАТИВКА', blank=True, null=True, max_length=1000)  # Field name made lowercase.
	
	fns = models.CharField(db_column='ФНС', blank=True, null=True, max_length=1000)  # Field name made lowercase.
	data_pisma_v_fns = models.CharField(db_column='ДАТА_ПИСЬМА_В_ФНС', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_pisma_v_fns = models.CharField(db_column='НОМЕР_ПИСЬМА_В_ФНС', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	informaciya_o_poluchenii_otveta_ot_fns = models.CharField(db_column='ИНФОРМАЦИЯ_О_ПОЛУЧЕНИИ_ОТВЕТА_ОТ_ФНС', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	vh_nomer_otveta = models.CharField(db_column='ВХ_НОМЕР_ОТВЕТА', blank=True, null=True,max_length=1000,)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	soderzhanie_otveta = models.CharField(db_column='СОДЕРЖАНИЕ_ОТВЕТА', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	otvet_fns_ob_adrese = models.CharField(db_column='ОТВЕТ_ФНС_ОБ_АДРЕСЕ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove = models.CharField(db_column='ВЗАИМОДЕЙСТВИЕ_С_ФНС_НА_ЕЖЕКВАРТАЛЬНОЙ_ОСНОВЕ', blank=True, null=True, max_length=1000)
	vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_nomer_pisma = models.CharField(db_column='ВЗАИМОДЕЙСТВИЕ_С_ФНС_НА_ЕЖЕКВАРТАЛЬНОЙ_ОСНОВЕ_НОМЕР_ПИСЬМА', blank=True, null=True, max_length=1000)
	vzaimodeystvie_s_fns_na_ezhekvartalnoi_osnove_data_pisma = models.CharField(db_column='ВЗАИМОДЕЙСТВИЕ_С_ФНС_НА_ЕЖЕКВАРТАЛЬНОЙ_ОСНОВЕ_ДАТА_ПИСЬМА', blank=True, null=True, max_length=1000)
	svedeniya_ob_adrese_ne_dostoverny = models.CharField(db_column='СВЕДЕНИЯ_ОБ_АДРЕСЕ_НЕ_ДОСТОВЕРНЫ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_vneseniya_zapisi = models.CharField(db_column='ДАТА_ВНЕСЕНИЯ_ЗАПИСИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	vzaimodeystvie_s_gos_organami = models.CharField(db_column='ВЗАИМОДЕЙСТВИЕ_С_ГОС_ОРГАНАМИ', blank=True, null=True, max_length=1000)  # Field name made lowercase. Field renamed to remove unsuitable characters.

	class Meta:
		managed = False
		db_table = 'Data111'


class Data222(models.Model):
	id = models.IntegerField(unique=True, blank=True, primary_key=True)
	naimenovanie = models.CharField(db_column='НАИМЕНОВАНИЕ', blank=True, null=True, max_length=1000, default=None)  # Field name made lowercase.
	inn = models.CharField(db_column='ИНН', blank=True, null=True, max_length=10, default=None)  # Field name made lowercase.
	ogrn = models.CharField(db_column='ОГРН', blank=True, null=True, max_length=30, default=None)  # Field name made lowercase.
	data_registracii = models.TextField(db_column='ДАТА РЕГИСТРАЦИИ', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	opf = models.TextField(db_column='ОПФ', blank=True, null=True, default=None)  # Field name made lowercase.
	cod_emitenta = models.CharField(db_column='КОД ЭМИТЕНТА', blank=True, null=True, max_length=7, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	ustavnoy_capital = models.TextField(db_column='УСТАВНОЙ КАПИТАЛ', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	kolichestvo_licevyh_schetov_v_reestre = models.TextField(db_column='Количество лицевых счетов в реестре', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	kolichestvo_nominalnyh_derzhateley_v_reestre = models.TextField(db_column='Количество номинальных держателей в реестре', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	cvedeniya_ob_otritii_scheta_nominalnogo_derzhatelya_centralnogo_depozitoria = models.TextField(db_column='Сведения об открытии счета номинального держателя центрального депозитария', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	region = models.TextField(db_column='РЕГИОН', blank=True, null=True, default=None)  # Field name made lowercase.
	adres = models.TextField(db_column='АДРЕС', blank=True, null=True, default=None)  # Field name made lowercase.
	edinolichny_ispolnitelny_organ = models.TextField(db_column='ЕДИНОЛИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ ОРГАН', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	contactny_dannye = models.TextField(db_column='КОНТАКТНЫЕ ДАННЫЕ', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	status = models.TextField(db_column='СТАТУС', blank=True, null=True, default=None)  # Field name made lowercase.
	dvizhenie_denezhnyh_sredstv = models.TextField(db_column='ДВИЖЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	otchetnost = models.TextField(db_column='ОТЧЕТНОСТЬ', blank=True, null=True, default=None)  # Field name made lowercase.
	zadolzhennost_pered_fns = models.TextField(db_column='ЗАДОЛЖЕННОСТЬ ПЕРЕД ФНС', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	kartochka_kompanii = models.TextField(db_column='КАРТОЧКА КОМПАНИИ', blank=True, null=True, default=None)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	registrator = models.TextField(db_column='РЕГИСТРАТОР', blank=True, null=True)  # Field name made lowercase.
	data_pisma_po_reestru = models.TextField(db_column='ДАТА ПИСЬМА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_pisma_po_reestru = models.TextField(db_column='НОМЕР ПИСЬМА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_po_reestru = models.TextField(db_column='ДАТА ЗАПРОСА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_po_reestru = models.TextField(db_column='НОМЕР ЗАПРОСА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_predpisanya_po_reestru = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_predpisaniya_po_reestru = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_provedeniya_gosa = models.TextField(db_column='ДАТА ПРОВЕДЕНИЯ ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_po_gosa = models.TextField(db_column='ДАТА ЗАПРОСА ПО ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_po_gosa = models.TextField(db_column='НОМЕР ЗАПРОСА ПО ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_predpisaniya_po_1_vypusku = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_predpisaniya_po_1_vypusku = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nrd = models.TextField(db_column='НРД', blank=True, null=True)  # Field name made lowercase.
	oao_na_22_06_2015 = models.TextField(db_column='ОАО на 22.06.2015', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	korp_kontrol = models.TextField(db_column='КОРП КОНТРОЛЬ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	pao_v_silu_priznakov = models.TextField(db_column='ПАО В СИЛУ ПРИЗНАКОВ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	pao_v_silu_nazvaniya = models.TextField(db_column='ПАО В СИЛУ НАЗВАНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nao_obyazannoe_raskryvat_informaciyu_v_sootvetstvii_so_st_30_fz_o_pcb = models.TextField(db_column='НАО ОБЯЗАННОЕ РАСКРЫВАТЬ ИНФОРМАЦИЮ В СООТВЕТСТВИИ СО СТ.30 ФЗ О РЦБ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nao_osuchestvivshee_osuchestvlyayuschee_publichnoe_razmechenie_obligaciy_ili_inyh_cennyh_bumag = models.TextField(db_column='НАО ОСУЩЕСТВИВШЕЕ (ОСУЩЕСТВЛЯЮЩЕЕ) ПУБЛИЧНОЕ РАЗМЕЩЕНИЕ ОБЛИГАЦИЙ ИЛИ ИНЫХ ЦЕННЫХ БУМАГ ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
	nao = models.TextField(db_column='НАО', blank=True, null=True)  # Field name made lowercase.
	osvobozhdeny_ot_raskrytiya = models.TextField(db_column='ОСВОБОЖДЕНЫ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_resheniya_ob_osvobozhdenii = models.TextField(db_column='ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_resheniya_ob_osvobozhdenii = models.TextField(db_column='НОМЕР РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	otkaz_v_osvobozhdenii_ot_raskritiya = models.TextField(db_column='ОТКАЗ В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_otkaza_v_osvobozhdenii_ot_raskritiya = models.TextField(db_column='ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_otkaza_v_osvobozhdenii_ot_raskritiya = models.TextField(db_column='НОМЕР ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	proverka_raskritiya = models.TextField(db_column='ПРОВЕРКА РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_proverki = models.TextField(db_column='ДАТА ПРОВЕРКИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_po_neraskritiyu_informacii = models.TextField(db_column='ДАТА ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_po_neraskritiyu_informacii = models.TextField(db_column='НОМЕР ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_predpisaniya_po_neraskritiyu_informacii = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_predpisaniya_po_neraskritiyu_informacii = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.TextField(db_column='ДАТА ЗАПРОСА ОРЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.TextField(db_column='НОМЕР ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.TextField(db_column='ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_otveta_na_zaprosa_o_rezultatah_provedeniya_torgov_v_obchestve = models.TextField(db_column='НОМЕР ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	vivod = models.TextField(db_column='ВЫВОД', blank=True, null=True)  # Field name made lowercase.
	raskritie = models.TextField(db_column='РАСКРЫТИЕ', blank=True, null=True)  # Field name made lowercase.
	data_protokola = models.TextField(db_column='ДАТА ПРОТОКОЛА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_protokola = models.TextField(db_column='НОМЕР ПРОТОКОЛА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	statya_koap = models.TextField(db_column='СТАТЬЯ КОАП', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_postanovleniya = models.TextField(db_column='ДАТА ПОСТАНОВЛЕНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_postanovleniya = models.TextField(db_column='НОМЕР ПОСТАНОВЛЕНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	resultat = models.TextField(db_column='РЕЗУЛЬТАТ', blank=True, null=True)  # Field name made lowercase.
	razmer_shtrafa = models.TextField(db_column='РАЗМЕР ШТРАФА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	administrativka = models.TextField(db_column='АДМИНИСТРАТИВКА', blank=True, null=True)  # Field name made lowercase.
	fns = models.TextField(db_column='ФНС', blank=True, null=True)  # Field name made lowercase.
	data_pisma_v_fns = models.TextField(db_column='ДАТА ПИСЬМА В ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	nomer_pisma_v_fns = models.TextField(db_column='НОМЕР ПИСЬМА В ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	informaciya_o_poluchenii_otveta_ot_fns = models.TextField(db_column='ИНФОРМАЦИЯ О ПОЛУЧЕНИИ ОТВЕТА ОТ ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	vh_nomer_otveta = models.TextField(db_column='ВХ. НОМЕР ОТВЕТА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	svedeniya_ob_adrese_ne_dostoverny = models.TextField(db_column='СВЕДЕНИЯ ОБ АДРЕСЕ НЕ ДОСТОВЕРНЫ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	data_vneseniya_zapisi = models.TextField(db_column='ДАТА ВНЕСЕНИЯ ЗАПИСИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
	vzaimodeystvie_s_gos_organami = models.TextField(db_column='ВЗАИМОДЕЙСТВИЕ С ГОС. ОРГАНАМИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

	vozvrat = models.BooleanField()
	class Meta:
		managed = False
		db_table = 'Data222'


class DjangoAdminLog(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	object_id = models.TextField(blank=True, null=True)
	object_repr = models.CharField(max_length=200)
	action_flag = models.PositiveSmallIntegerField()
	change_message = models.TextField()
	content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
	user = models.ForeignKey(AuthUser, models.DO_NOTHING)
	action_time = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_admin_log'


class DjangoContentType(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	app_label = models.CharField(max_length=100)
	model = models.CharField(max_length=100)

	class Meta:
		managed = False
		db_table = 'django_content_type'
		unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	app = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	applied = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_migrations'


class DjangoSession(models.Model):
	session_key = models.CharField(primary_key=True, max_length=40)
	session_data = models.TextField()
	expire_date = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'django_session'


def path_and_rename(path):
    def wrap(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(instance.db, ext)        
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrap


'''class UpdateDB(models.Model):
    db_file = models.FileField(upload_to=path_and_rename(''))       
    db = 'database'''

class Document(models.Model):
    db = 'DB'
    #docfile = models.FileField(upload_to=path_and_rename('{}/{}/{}/'.format(now.year, now.month, now.day)))
    docfile = models.FileField(upload_to=path_and_rename(''))




    