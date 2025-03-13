from django.shortcuts import render
from django.http import HttpResponse

def login(request):
	return HttpResponse("Hello, word. You're at the users index")
