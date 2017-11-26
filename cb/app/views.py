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
            queryset = Data111.objects.all().filter(naimenovanie__icontains = form['naimenovanie'].value(), inn__icontains = form['inn'].value(), ogrn__icontains = form['ogrn'].value(), cod_emitenta__icontains = form['cod_emitenta'].value() )
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


def selections(request):
    a = []
    form = Data111FormSelection(request.POST or None)
    context = {
		"form": form,
	}
    if request.method == 'POST':
        for i in form._meta.fields:
            if form[i].value():
                a.append(i)
        context = {
    		"form": form,
            "a": a,
    	}
    return render(request, 'selections.html', context)


def home(request):
	title = 'Добро пожаловать'
	context = {
		"title": title,
	}
	return render(request, "base.html",context)
