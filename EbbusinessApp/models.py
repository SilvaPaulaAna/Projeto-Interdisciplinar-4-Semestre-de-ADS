

from django.db import models

class cliente(models.Model):
    empresa = models.CharField(max_length=15)
    nomeContato = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=19)
    rua = models.CharField(max_length=40)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=25)
    cidade = models.CharField(max_length=22)
    uf = models.CharField(max_length=2) #ESTADO
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=14)
    email = models.EmailField()
    #plano =    #LINK com a classe PLANOS
    #assinatura =   #LINK com a classe ASSINATURAS


#class preco


#class contrato







### ======================== TESTS
#cnpj(19) 05.454.389/0001-69
#cidade(22) sao jose do rio preto
#cep(10) 13348-090
#telefone(14) 19 99377-6771