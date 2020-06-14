from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import DadosEmpresas, ContratoForm
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
            return render(request, 'salvo.html')
    
    form = DadosEmpresas()
    return render(request, 'contratar.html', {'form':form})


def fale_conosco(request):
    return render(request, 'fale_conosco.html')

def salvo(request):
    return render(request, 'salvo.html')






