from django.shortcuts import render

# Create your views here.

def search(request):
	return render(request, 'search.html', locals())

def selections(request):
	return render(request, 'selections.html', locals())