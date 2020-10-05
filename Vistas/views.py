from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
# Create your views here.
def login(request):
	doc_externo = loader.get_template("login.html")
	documento = doc_externo.render()
	return HttpResponse(documento)