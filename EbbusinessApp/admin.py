from django.contrib import admin
from EbbusinessApp.models import Assinaturas, Empresas, Planos

# Register your models here.
# Login = admin
# Passwd = Brasil22020

admin.site.register(Assinaturas)
admin.site.register(Empresas)
admin.site.register(Planos)