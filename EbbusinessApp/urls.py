from django.conf.urls import url
from EbbusinessApp.views import index
from EbbusinessApp.views import a_empresa
from EbbusinessApp.views import nossos_planos
from EbbusinessApp.views import fale_conosco
from EbbusinessApp.views import contratar
from EbbusinessApp.views import salvo

urlpatterns = [
    url(r'^index/', index, name='index'),
    url(r'^a_empresa/', a_empresa, name='a_empresa'),
    url(r'^nossos_planos/', nossos_planos, name='nossos_planos'),
    url(r'^fale_conosco/', fale_conosco, name='fale_conosco'),
    url(r'^contratar/', contratar, name='contratar'),
    url(r'^salvo/', salvo, name='salvo'),
]