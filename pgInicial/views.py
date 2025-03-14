from django.shortcuts import render

def index(request):
	"""A pagina inicial de Garimpo"""
	return render(request, "pgInicial/index.html")
