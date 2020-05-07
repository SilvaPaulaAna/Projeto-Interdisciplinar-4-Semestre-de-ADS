from django.forms import ModelForm
from EbbusinessApp.models import Contratar
from EbbusinessApp.models import Fale_Conosco

class ContratarForm(ModelForm):
    class Meta:
        model = Contratar
        fields = ['empresa','cnpj','telefone','logradouro','numero_endereco','complemento_endereco','cidade','estado','email']

class Fale_ConoscoForm(ModelForm):
    class Meta:
        model = Fale_Conosco
        fields = ['empresa','email','mensagem']
