# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('empresa', models.CharField(verbose_name='Empresa:', max_length=50)),
                ('cnpj', models.CharField(verbose_name='CNPJ:', max_length=18)),
                ('telefone', models.CharField(verbose_name='Telefone', max_length=19)),
                ('logradouro', models.CharField(verbose_name='Rua:', max_length=50)),
                ('numero_endereco', models.PositiveIntegerField(verbose_name='Nº:')),
                ('complemento_endereco', models.CharField(verbose_name='Complemento:', max_length=50, null=True)),
                ('cidade', models.CharField(verbose_name='Cidade:', max_length=40)),
                ('estado', models.CharField(verbose_name='Estado', max_length=15)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fale_Conosco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('empresa', models.CharField(verbose_name='Empresa:', max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mensagem', models.TextField(verbose_name='Mensagem:', max_length=200)),
            ],
        ),
    ]
