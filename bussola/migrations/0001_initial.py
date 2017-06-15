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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('numeroEstrelas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('bairro', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('cidade', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comenta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricaoContato', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('bairro', models.ForeignKey(verbose_name='Bairro', to='bussola.Bairro', null=True)),
                ('cidade', models.ForeignKey(verbose_name='Cidade', to='bussola.Cidade', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaleConosco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('mensagem', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FazComentario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comentario', models.ForeignKey(verbose_name='Comentario', to='bussola.Comentario', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('descricaoImagem', models.ImageField(max_length=200, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Realiza',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('avaliacao', models.ForeignKey(verbose_name='Avaliacao', to='bussola.Avaliacao', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nomeServico', models.CharField(max_length=200)),
                ('informacoesServico', models.CharField(max_length=200)),
                ('informacoesPreco', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(verbose_name='Categoria', to='bussola.Categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoContato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
            model_name='realiza',
            name='usuario',
            field=models.ForeignKey(verbose_name='Usuario', to='bussola.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='imagens',
            name='servico',
            field=models.ForeignKey(verbose_name='Servico', to='bussola.Servico', null=True),
        ),
        migrations.AddField(
            model_name='fazcomentario',
            name='usuario',
            field=models.ForeignKey(verbose_name='Usuario', to='bussola.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='rua',
            field=models.ForeignKey(verbose_name='Rua', to='bussola.Rua', null=True),
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
            model_name='comenta',
            name='comentario',
            field=models.ForeignKey(verbose_name='Comentario', to='bussola.Comentario', null=True),
        ),
        migrations.AddField(
            model_name='comenta',
            name='servico',
            field=models.ForeignKey(verbose_name='Servico', to='bussola.Servico', null=True),
        ),
        migrations.AddField(
            model_name='avalia',
            name='avaliacao',
            field=models.ForeignKey(verbose_name='Avaliacao', to='bussola.Avaliacao', null=True),
        ),
        migrations.AddField(
            model_name='avalia',
            name='servico',
            field=models.ForeignKey(verbose_name='Servico', to='bussola.Servico', null=True),
        ),
    ]
