# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('descricaoContato', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('cidade', models.ForeignKey(null=True, verbose_name='Cidade', to='bussola.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('descricaoImagem', models.ImageField(null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('endereco', models.ForeignKey(null=True, verbose_name='Endereco', to='bussola.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nomeServico', models.CharField(max_length=200)),
                ('informacoesServico', models.CharField(max_length=200)),
                ('informacoesPreco', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(null=True, verbose_name='Categoria', to='bussola.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cpfCnpj', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='usuario',
            field=models.ForeignKey(null=True, verbose_name='Usuario', to='bussola.Usuario'),
        ),
        migrations.AddField(
            model_name='imagens',
            name='servico',
            field=models.ForeignKey(null=True, verbose_name='Servico', to='bussola.Servico'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='servico',
            field=models.ForeignKey(null=True, verbose_name='Servico', to='bussola.Servico'),
        ),
        migrations.AddField(
            model_name='contato',
            name='servico',
            field=models.ForeignKey(null=True, verbose_name='Servico', to='bussola.Servico'),
        ),
        migrations.AddField(
            model_name='contato',
            name='tipo',
            field=models.ForeignKey(null=True, verbose_name='TipoContato', to='bussola.TipoContato'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='endereco',
            field=models.ForeignKey(null=True, verbose_name='Endereco', to='bussola.Endereco'),
        ),
    ]
