from django import forms
from .models import Empresas
from bootstrap_modal_forms.forms import BSModalForm

class ContratoForm(BSModalForm):
    class Meta:
        model = Empresas
        fields = ['nomeEmpresa', 'numeroCnpj', 'plano', 'assinatura',]
        labels = {
            'nomeEmpresa':'Empresa',            
            'numeroCnpj':'CNPJ',            
            'plano':'Planos',
            'assinatura':'Assinaturas',
        }

class DadosEmpresas(forms.ModelForm):
    confirmaInformacao = forms.BooleanField(label='Confirmo que todas as informações acima são verdadeiras.')
    confirmaContrato = forms.BooleanField(label='Confirmo que li e estou de acordo com os termos do contrato.')
    class Meta:        
        model = Empresas
        fields = ('nomeEmpresa', 'nomeContato',
        'numeroCnpj', 'enderecoRua', 'enderecoNumero', 'enderecoComplemento',
        'cidade', 'estados', 'numeroCep', 'numetoTelefone', 'email', 'plano', 'assinatura',)
        labels = {
            'nomeEmpresa':'Empresa',
            'nomeContato':'Nome para contato',
            'numeroCnpj':'CNPJ',
            'enderecoRua':'Rua',
            'enderecoNumero':'Número',
            'enderecoComplemento':'Complemento',
            'cidade':'Cidade',
            'estados':'Estado',
            'numeroCep':'CEP',
            'numetoTelefone':'Telefone',
            'email':'Email',
            'plano':'Planos',
            'assinatura':'Assinaturas',
        }
        
