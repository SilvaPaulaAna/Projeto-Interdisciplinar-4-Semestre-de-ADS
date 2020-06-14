from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def a_empresa(request):
    return render(request, 'a_empresa.html')

def nossos_planos(request):
    return render(request, 'nossos_planos.html')

def contratar(request):
    return render(request, 'contratar.html')


def fale_conosco(request):
    return render(request, 'fale_conosco.html')

def salvo(request):
    return render(request, 'salvo.html')






