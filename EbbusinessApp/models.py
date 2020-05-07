from django.db import models

class Contratar(models.Model):
    empresa = models.CharField(max_length=50, null=False, verbose_name='Empresa:')
    cnpj = models.CharField(max_length=18, null=False, verbose_name='CNPJ:')
    telefone = models.CharField(max_length=19, null=False, verbose_name='Telefone')
    logradouro = models.CharField(max_length=50, null=False, verbose_name='Rua:')
    numero_endereco = models.PositiveIntegerField(null=False, verbose_name='Nº:')
    complemento_endereco = models.CharField(max_length=50, null= True , verbose_name='Complemento:')
    cidade = models.CharField(max_length=40, null=False, verbose_name='Cidade:')
    estado = models.CharField(max_length=15, null=False, verbose_name='Estado')  
    email = models.EmailField(max_length=50, null=False)

class Fale_Conosco(models.Model):
    empresa = models.CharField(max_length=50, null=False, verbose_name='Empresa:')
    email = models.EmailField(max_length=50, null=False)
    mensagem = models.TextField(max_length=200, null=False, verbose_name='Mensagem:')
   
