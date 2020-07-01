
from django.db import models

# Create your models here.

class Planos(models.Model):
    planos = models.CharField(max_length=100)

    def __str__(self):
        return self.planos

class Assinaturas(models.Model):
    assinaturas = models.CharField(max_length=100)

    def __str__(self):
        return self.assinaturas

class Empresas(models.Model):
    nomeEmpresa = models.CharField(max_length=100)
    nomeContato = models.CharField(max_length=100)
    numeroCnpj = models.CharField(max_length=18, primary_key=True)
    enderecoRua = models.CharField(max_length=100)
    enderecoNumero = models.CharField(max_length=10)
    enderecoComplemento = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100)
    numeroCep = models.CharField(max_length=10)
    numetoTelefone = models.CharField(max_length=14)
    email = models.EmailField()
    plano = models.ForeignKey(Planos, on_delete=models.CASCADE)
    assinatura = models.ForeignKey(Assinaturas, on_delete=models.CASCADE)    
    estadosBrasileiros = [
    ('', 'Escolher...'),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
    ]
    estados = models.CharField(max_length=2, choices=estadosBrasileiros, default='')

class Contato(models.Model):
    contatoNome = models.CharField(max_length=100)
    contatoEmail = models.EmailField()
    contatoMensagem = models.TextField()