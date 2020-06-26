from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import DadosEmpresas, ContratoForm, DadosContato
from bootstrap_modal_forms.generic import BSModalCreateView

class CreatePopUpView(BSModalCreateView):
    template_name = 'contrato.html'
    form_class = ContratoForm    

def index(request):
    return render(request, 'index.html')

def a_empresa(request):
    return render(request, 'a_empresa.html')

def nossos_planos(request):
    return render(request, 'nossos_planos.html')

def contratar(request):
    if request.method == 'POST':
        form = DadosEmpresas(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo_contrato.html')
    
    form = DadosEmpresas()
    return render(request, 'contratar.html', {'form':form})

def fale_conosco(request):
    if request.method == 'POST':
        form = DadosContato(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'salvo_mensagem.html')
    
    form = DadosContato()
    return render(request, 'fale_conosco.html', {'form':form})

def salvo(request):
    return render(request, 'salvo.html')
