from django.shortcuts import render, redirect

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
        if form['наименование'].value() == '' and form['инн'].value() == '' and form['огрн'].value() == '' and form['код_эмитента'].value() == '':
            queryset = None
        else:
            queryset = Data111.objects.all().order_by('-id').filter(наименование__icontains = form['наименование'].value(), инн__icontains = form['инн'].value(), огрн__icontains = form['огрн'].value(), код_эмитента__icontains = form['код_эмитента'].value() )
        context = {
			"queryset": queryset,
			"form": form,
			}
    return render(request, 'search.html', context)


def edit(request):
	return render(request, 'edit.html')


def selections(request):
	return render(request, 'selections.html', locals())

def home(request):
	title = 'Добро пожаловать'
	context = {
		"title": title,
	}
	return render(request, "base.html",context)
