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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('bairro', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=200)),
                ('imagemCategoria', models.ImageField(null=True, upload_to='categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('descricaoContato', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('cidade', models.ForeignKey(verbose_name='Cidade', to='bussola.Cidade', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('descricaoImagem', models.ImageField(null=True, upload_to='fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rua', models.CharField(max_length=200)),
                ('bairro', models.ForeignKey(verbose_name='Bairro', to='bussola.Bairro', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nomeServico', models.CharField(max_length=200)),
                ('informacoesServico', models.CharField(max_length=200)),
                ('informacoesPreco', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(verbose_name='Categoria', to='bussola.Categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cpfCnpj', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='usuario',
            field=models.ForeignKey(verbose_name='Usuario', to='bussola.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='imagens',
            name='servico',
            field=models.ForeignKey(verbose_name='Servico', to='bussola.Servico', null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='servico',
            field=models.ForeignKey(verbose_name='Servico', to='bussola.Servico', null=True),
        ),
        migrations.AddField(
            model_name='contato',
            name='servico',
            field=models.ForeignKey(verbose_name='Servico', to='bussola.Servico', null=True),
        ),
        migrations.AddField(
            model_name='contato',
            name='tipo',
            field=models.ForeignKey(verbose_name='TipoContato', to='bussola.TipoContato', null=True),
        ),
        migrations.AddField(
            model_name='bairro',
            name='endereco',
            field=models.ForeignKey(verbose_name='Endereco', to='bussola.Endereco', null=True),
        ),
    ]
