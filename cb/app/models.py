# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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
    id = models.IntegerField(unique=True, blank=True, primary_key=True)
    наименование = models.CharField(db_column='НАИМЕНОВАНИЕ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    инн = models.CharField(db_column='ИНН', blank=True, null=True, max_length=10)  # Field name made lowercase.
    огрн = models.CharField(db_column='ОГРН', blank=True, null=True, max_length=30)  # Field name made lowercase.
    дата_регистрации = models.TextField(db_column='ДАТА РЕГИСТРАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    опф = models.TextField(db_column='ОПФ', blank=True, null=True)  # Field name made lowercase.
    код_эмитента = models.CharField(db_column='Код эмитента', blank=True, null=True, max_length=7)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    уставной_капитал = models.TextField(db_column='УСТАВНОЙ КАПИТАЛ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    количество_лицевых_счетов_в_реестре = models.TextField(db_column='Количество лицевых счетов в реестре', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    количество_номинальных_держателей_в_реестре = models.TextField(db_column='Количество номинальных держателей в реестре', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    сведения_об_открытии_счета_номинального_держателя_центрального_депозитария = models.TextField(db_column='Сведения об открытии счета номинального держателя центрального депозитария', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    регион = models.TextField(db_column='РЕГИОН', blank=True, null=True)  # Field name made lowercase.
    адрес = models.TextField(db_column='АДРЕС', blank=True, null=True)  # Field name made lowercase.
    единоличный_исполнительный_орган = models.TextField(db_column='ЕДИНОЛИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ ОРГАН', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    контактные_данные = models.TextField(db_column='КОНТАКТНЫЕ ДАННЫЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    статус = models.TextField(db_column='СТАТУС', blank=True, null=True)  # Field name made lowercase.
    движение_денежных_средств = models.TextField(db_column='ДВИЖЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    отчетность = models.TextField(db_column='ОТЧЕТНОСТЬ', blank=True, null=True)  # Field name made lowercase.
    задолженность_перед_фнс = models.TextField(db_column='ЗАДОЛЖЕННОСТЬ ПЕРЕД ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    карточка_компании = models.TextField(db_column='КАРТОЧКА КОМПАНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    регистратор = models.TextField(db_column='РЕГИСТРАТОР', blank=True, null=True)  # Field name made lowercase.
    дата_письма_по_реестру = models.TextField(db_column='ДАТА ПИСЬМА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_письма_по_реестру = models.TextField(db_column='НОМЕР ПИСЬМА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_по_реестру = models.TextField(db_column='ДАТА ЗАПРОСА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_по_реестру = models.TextField(db_column='НОМЕР ЗАПРОСА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_предписания_по_реестру = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_предписания_по_реестру = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_проведения_госа = models.TextField(db_column='ДАТА ПРОВЕДЕНИЯ ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_по_госа = models.TextField(db_column='ДАТА ЗАПРОСА ПО ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_по_госа = models.TextField(db_column='НОМЕР ЗАПРОСА ПО ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_предписания_по_1_выпуску = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_предписания_по_1_выпуску = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    нрд = models.TextField(db_column='НРД', blank=True, null=True)  # Field name made lowercase.
    оао_на_22_06_2015 = models.TextField(db_column='ОАО на 22.06.2015', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    корп_контроль = models.TextField(db_column='КОРП КОНТРОЛЬ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    пао_в_силу_признаков = models.TextField(db_column='ПАО В СИЛУ ПРИЗНАКОВ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    пао_в_силу_названия = models.TextField(db_column='ПАО В СИЛУ НАЗВАНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    нао_обязанное_раскрывать_информацию_в_соответствии_со_ст_30_фз_о_рцб = models.TextField(db_column='НАО ОБЯЗАННОЕ РАСКРЫВАТЬ ИНФОРМАЦИЮ В СООТВЕТСТВИИ СО СТ.30 ФЗ О РЦБ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    нао_осуществившее_осуществляющее_публичное_размещение_облигаций_или_иных_ценных_бумаг_field = models.TextField(db_column='НАО ОСУЩЕСТВИВШЕЕ (ОСУЩЕСТВЛЯЮЩЕЕ) ПУБЛИЧНОЕ РАЗМЕЩЕНИЕ ОБЛИГАЦИЙ ИЛИ ИНЫХ ЦЕННЫХ БУМАГ ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    нао = models.TextField(db_column='НАО', blank=True, null=True)  # Field name made lowercase.
    освобождены_от_раскрытия = models.TextField(db_column='ОСВОБОЖДЕНЫ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_решения_об_освобождении = models.TextField(db_column='ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_решения_об_освобождении = models.TextField(db_column='НОМЕР РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    отказ_в_освобождении_от_раскрытия = models.TextField(db_column='ОТКАЗ В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_отказа_в_освобождении_от_раскрытия = models.TextField(db_column='ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_отказа_в_освобождении_от_раскрытия = models.TextField(db_column='НОМЕР ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    проверка_раскрытия = models.TextField(db_column='ПРОВЕРКА РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_проверки = models.TextField(db_column='ДАТА ПРОВЕРКИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_по_нераскрытию_информации = models.TextField(db_column='ДАТА ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_по_нераскрытию_информации = models.TextField(db_column='НОМЕР ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_предписания_по_нераскрытию_информации = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_предписания_по_нераскрытию_информации = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_орезультатах_проведения_торгов_в_обществе = models.TextField(db_column='ДАТА ЗАПРОСА ОРЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_о_результатах_проведения_торгов_в_обществе = models.TextField(db_column='НОМЕР ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_ответа_на_запроса_о_результатах_проведения_торгов_в_обществе = models.TextField(db_column='ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_ответа_на_запроса_о_результатах_проведения_торгов_в_обществе = models.TextField(db_column='НОМЕР ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    вывод = models.TextField(db_column='ВЫВОД', blank=True, null=True)  # Field name made lowercase.
    раскрытие = models.TextField(db_column='РАСКРЫТИЕ', blank=True, null=True)  # Field name made lowercase.
    дата_протокола = models.TextField(db_column='ДАТА ПРОТОКОЛА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_протокола = models.TextField(db_column='НОМЕР ПРОТОКОЛА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    статья_коап = models.TextField(db_column='СТАТЬЯ КОАП', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_постановления = models.TextField(db_column='ДАТА ПОСТАНОВЛЕНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_постановления = models.TextField(db_column='НОМЕР ПОСТАНОВЛЕНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    результат = models.TextField(db_column='РЕЗУЛЬТАТ', blank=True, null=True)  # Field name made lowercase.
    размер_штрафа = models.TextField(db_column='РАЗМЕР ШТРАФА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    административка = models.TextField(db_column='АДМИНИСТРАТИВКА', blank=True, null=True)  # Field name made lowercase.
    фнс = models.TextField(db_column='ФНС', blank=True, null=True)  # Field name made lowercase.
    дата_письма_в_фнс = models.TextField(db_column='ДАТА ПИСЬМА В ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_письма_в_фнс = models.TextField(db_column='НОМЕР ПИСЬМА В ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    информация_о_получении_ответа_от_фнс = models.TextField(db_column='ИНФОРМАЦИЯ О ПОЛУЧЕНИИ ОТВЕТА ОТ ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    вх_номер_ответа = models.TextField(db_column='ВХ. НОМЕР ОТВЕТА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    сведения_об_адресе_не_достоверны = models.TextField(db_column='СВЕДЕНИЯ ОБ АДРЕСЕ НЕ ДОСТОВЕРНЫ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_внесения_записи = models.TextField(db_column='ДАТА ВНЕСЕНИЯ ЗАПИСИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    взаимодействие_с_гос_органами = models.TextField(db_column='ВЗАИМОДЕЙСТВИЕ С ГОС. ОРГАНАМИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'data111'


class Data222(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    наименование = models.TextField(db_column='НАИМЕНОВАНИЕ', blank=True, null=True)  # Field name made lowercase.
    инн = models.TextField(db_column='ИНН', blank=True, null=True)  # Field name made lowercase.
    огрн = models.TextField(db_column='ОГРН', blank=True, null=True)  # Field name made lowercase.
    дата_регистрации = models.TextField(db_column='ДАТА РЕГИСТРАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    опф = models.TextField(db_column='ОПФ', blank=True, null=True)  # Field name made lowercase.
    код_эмитента = models.TextField(db_column='КОД ЭМИТЕНТА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    уставной_капитал = models.TextField(db_column='УСТАВНОЙ КАПИТАЛ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    количество_лицевых_счетов_в_реестре = models.TextField(db_column='Количество лицевых счетов в реестре', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    количество_номинальных_держателей_в_реестре = models.TextField(db_column='Количество номинальных держателей в реестре', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    сведения_об_открытии_счета_номинального_держателя_центрального_депозитария = models.TextField(db_column='Сведения об открытии счета номинального держателя центрального депозитария', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    регион = models.TextField(db_column='РЕГИОН', blank=True, null=True)  # Field name made lowercase.
    адрес = models.TextField(db_column='АДРЕС', blank=True, null=True)  # Field name made lowercase.
    единоличный_исполнительный_орган = models.TextField(db_column='ЕДИНОЛИЧНЫЙ ИСПОЛНИТЕЛЬНЫЙ ОРГАН', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    контактные_данные = models.TextField(db_column='КОНТАКТНЫЕ ДАННЫЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    статус = models.TextField(db_column='СТАТУС', blank=True, null=True)  # Field name made lowercase.
    движение_денежных_средств = models.TextField(db_column='ДВИЖЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    отчетность = models.TextField(db_column='ОТЧЕТНОСТЬ', blank=True, null=True)  # Field name made lowercase.
    задолженность_перед_фнс = models.TextField(db_column='ЗАДОЛЖЕННОСТЬ ПЕРЕД ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    карточка_компании = models.TextField(db_column='КАРТОЧКА КОМПАНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    регистратор = models.TextField(db_column='РЕГИСТРАТОР', blank=True, null=True)  # Field name made lowercase.
    дата_письма_по_реестру = models.TextField(db_column='ДАТА ПИСЬМА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_письма_по_реестру = models.TextField(db_column='НОМЕР ПИСЬМА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_по_реестру = models.TextField(db_column='ДАТА ЗАПРОСА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_по_реестру = models.TextField(db_column='НОМЕР ЗАПРОСА ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_предписания_по_реестру = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_предписания_по_реестру = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО РЕЕСТРУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_проведения_госа = models.TextField(db_column='ДАТА ПРОВЕДЕНИЯ ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_по_госа = models.TextField(db_column='ДАТА ЗАПРОСА ПО ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_по_госа = models.TextField(db_column='НОМЕР ЗАПРОСА ПО ГОСА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_предписания_по_1_выпуску = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_предписания_по_1_выпуску = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО 1 ВЫПУСКУ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    нрд = models.TextField(db_column='НРД', blank=True, null=True)  # Field name made lowercase.
    оао_на_22_06_2015 = models.TextField(db_column='ОАО на 22.06.2015', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    корп_контроль = models.TextField(db_column='КОРП КОНТРОЛЬ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    пао_в_силу_признаков = models.TextField(db_column='ПАО В СИЛУ ПРИЗНАКОВ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    пао_в_силу_названия = models.TextField(db_column='ПАО В СИЛУ НАЗВАНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    нао_обязанное_раскрывать_информацию_в_соответствии_сост_30_фз_о_рцб = models.TextField(db_column='НАО ОБЯЗАННОЕ РАСКРЫВАТЬ ИНФОРМАЦИЮ В СООТВЕТСТВИИ СОСТ.30 ФЗ О РЦБ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    нао_осуществившее_осуществляющее_публичное_размещение_облигаций_или_иных_ценных_бумаг_field = models.TextField(db_column='НАО ОСУЩЕСТВИВШЕЕ (ОСУЩЕСТВЛЯЮЩЕЕ) ПУБЛИЧНОЕ РАЗМЕЩЕНИЕ ОБЛИГАЦИЙ ИЛИ ИНЫХ ЦЕННЫХ БУМАГ ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    нао = models.TextField(db_column='НАО', blank=True, null=True)  # Field name made lowercase.
    освобождены_от_раскрытия = models.TextField(db_column='ОСВОБОЖДЕНЫ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_решения_об_освобождении = models.TextField(db_column='ДАТА РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_решения_об_освобождении = models.TextField(db_column='НОМЕР РЕШЕНИЯ ОБ ОСВОБОЖДЕНИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    отказ_в_освобождении_от_раскрытия = models.TextField(db_column='ОТКАЗ В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_отказа_в_освобождении_от_раскрытия = models.TextField(db_column='ДАТА ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_отказа_в_освобождении_от_раскрытия = models.TextField(db_column='НОМЕР ОТКАЗА В ОСВОБОЖДЕНИИ ОТ РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    проверка_раскрытия = models.TextField(db_column='ПРОВЕРКА РАСКРЫТИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_проверки = models.TextField(db_column='ДАТА ПРОВЕРКИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_по_нераскрытию_информации = models.TextField(db_column='ДАТА ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_по_нераскрытию_информации = models.TextField(db_column='НОМЕР ЗАПРОСА ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_предписания_по_нераскрытию_информации = models.TextField(db_column='ДАТА ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_предписания_по_нераскрытию_информации = models.TextField(db_column='НОМЕР ПРЕДПИСАНИЯ ПО НЕРАСКРЫТИЮ ИНФОРМАЦИИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_запроса_о_результатах_проведения_торгов_в_обществе = models.TextField(db_column='ДАТА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_запроса_о_результатах_проведения_торгов_в_обществе = models.TextField(db_column='НОМЕР ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_ответа_на_запроса_о_результатах_проведения_торгов_в_обществе = models.TextField(db_column='ДАТА ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_ответа_на_запроса_о_результатах_проведения_торгов_в_обществе = models.TextField(db_column='НОМЕР ОТВЕТА НА ЗАПРОСА О РЕЗУЛЬТАТАХ ПРОВЕДЕНИЯ ТОРГОВ В ОБЩЕСТВЕ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    вывод = models.TextField(db_column='ВЫВОД', blank=True, null=True)  # Field name made lowercase.
    раскрытие = models.TextField(db_column='РАСКРЫТИЕ', blank=True, null=True)  # Field name made lowercase.
    дата_протокола = models.TextField(db_column='ДАТА ПРОТОКОЛА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_протокола = models.TextField(db_column='НОМЕР ПРОТОКОЛА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    статья_коап = models.TextField(db_column='СТАТЬЯ КОАП', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_постановления = models.TextField(db_column='ДАТА ПОСТАНОВЛЕНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_постановления = models.TextField(db_column='НОМЕР ПОСТАНОВЛЕНИЯ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    результат = models.TextField(db_column='РЕЗУЛЬТАТ', blank=True, null=True)  # Field name made lowercase.
    размер_штрафа = models.TextField(db_column='РАЗМЕР ШТРАФА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    административка = models.TextField(db_column='АДМИНИСТРАТИВКА', blank=True, null=True)  # Field name made lowercase.
    фнс = models.TextField(db_column='ФНС', blank=True, null=True)  # Field name made lowercase.
    дата_письма_в_фнс = models.TextField(db_column='ДАТА ПИСЬМА В ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    номер_письма_в_фнс = models.TextField(db_column='НОМЕР ПИСЬМА В ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    информация_о_получении_ответа_от_фнс = models.TextField(db_column='ИНФОРМАЦИЯ О ПОЛУЧЕНИИ ОТВЕТА ОТ ФНС', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    вх_номер_ответа = models.TextField(db_column='ВХ. НОМЕР ОТВЕТА', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    сведения_об_адресе_не_достоверны = models.TextField(db_column='СВЕДЕНИЯ ОБ АДРЕСЕ НЕ ДОСТОВЕРНЫ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    дата_внесения_записи = models.TextField(db_column='ДАТА ВНЕСЕНИЯ ЗАПИСИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    взаимодействие_с_гос_органами = models.TextField(db_column='ВЗАИМОДЕЙСТВИЕ С ГОС. ОРГАНАМИ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'data222'


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
