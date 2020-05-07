from django.shortcuts import render, get_object_or_404, redirect
from EbbusinessApp.forms import ContratarForm
from EbbusinessApp.forms import Fale_ConoscoForm
from EbbusinessApp.models import Contratar
from EbbusinessApp.models import Fale_Conosco


def index(request):
    return render(request, 'index.html')

def a_empresa(request):
    return render(request, 'a_empresa.html')

def nossos_planos(request):
    return render(request, 'nossos_planos.html')

def contratar(request):
    if request.method == "POST": 
        form = ContratarForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return render(request, "salvo.html", {})
    else: 
        form = ContratarForm()
    return render(request, "contratar.html", {'form': form})

def fale_conosco(request):
    if request.method == "POST": 
        form = Fale_ConoscoForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return render(request, "salvo.html", {})
    else: 
        form = Fale_ConoscoForm()
    return render(request, "fale_conosco.html", {'form': form})

def salvo(request):
    return render(request, 'salvo.html')






