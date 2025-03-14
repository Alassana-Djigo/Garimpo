from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
	return render(request, "users/login.html")

def cadastro(request):
	return render(request, "users/cadastro.html")
