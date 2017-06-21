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
            name='Avalia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('numeroEstrelas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('bairro', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descricaoContato', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('numero', models.IntegerField()),
                ('bairro', models.ForeignKey(null=True, to='bussola.Bairro', verbose_name='Bairro')),
            ],
        ),
        migrations.CreateModel(
            name='FaleConosco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('email', models.CharField(max_length=200)),
                ('mensagem', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FazComentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comentario', models.ForeignKey(null=True, to='bussola.Comentario', verbose_name='Comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('descricaoImagem', models.ImageField(upload_to='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Realiza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('avaliacao', models.ForeignKey(null=True, to='bussola.Avaliacao', verbose_name='Avaliacao')),
            ],
        ),
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('rua', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nomeServico', models.CharField(max_length=200)),
                ('informacoesServico', models.CharField(max_length=200)),
                ('informacoesPreco', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(null=True, to='bussola.Categoria', verbose_name='Categoria')),
                ('cidade', models.ForeignKey(null=True, to='bussola.Cidade', verbose_name='Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('cpfCnpj', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='usuario',
            field=models.ForeignKey(null=True, to='bussola.Usuario', verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='realiza',
            name='usuario',
            field=models.ForeignKey(null=True, to='bussola.Usuario', verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='imagens',
            name='servico',
            field=models.ForeignKey(null=True, to='bussola.Servico', verbose_name='Servico'),
        ),
        migrations.AddField(
            model_name='fazcomentario',
            name='usuario',
            field=models.ForeignKey(null=True, to='bussola.Usuario', verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='rua',
            field=models.ForeignKey(null=True, to='bussola.Rua', verbose_name='Rua'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='servico',
            field=models.ForeignKey(null=True, to='bussola.Servico', verbose_name='Servico'),
        ),
        migrations.AddField(
            model_name='contato',
            name='servico',
            field=models.ForeignKey(null=True, to='bussola.Servico', verbose_name='Servico'),
        ),
        migrations.AddField(
            model_name='contato',
            name='tipo',
            field=models.ForeignKey(null=True, to='bussola.TipoContato', verbose_name='TipoContato'),
        ),
        migrations.AddField(
            model_name='comenta',
            name='comentario',
            field=models.ForeignKey(null=True, to='bussola.Comentario', verbose_name='Comentario'),
        ),
        migrations.AddField(
            model_name='comenta',
            name='servico',
            field=models.ForeignKey(null=True, to='bussola.Servico', verbose_name='Servico'),
        ),
        migrations.AddField(
            model_name='avalia',
            name='avaliacao',
            field=models.ForeignKey(null=True, to='bussola.Avaliacao', verbose_name='Avaliacao'),
        ),
        migrations.AddField(
            model_name='avalia',
            name='servico',
            field=models.ForeignKey(null=True, to='bussola.Servico', verbose_name='Servico'),
        ),
    ]
