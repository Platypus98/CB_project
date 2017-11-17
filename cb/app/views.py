from django.shortcuts import render

from .forms import *

# Create your views here.

def search(request):
	form = Data111Form
	return render(request, 'search.html',{'form': form})

def selections(request):
	return render(request, 'selections.html', locals())

def home(request):
	title = 'Добро пожаловать'
	context = {
		"title": title,
	}
	return render(request, "base.html",context)
