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
            name='Avalia_local',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao_estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('numero_estrelas_est', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao_servico',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('numero_estrelas_ser', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao_sobre_ser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('avaliacao_servico', models.ForeignKey(to='bussola.Avaliacao_servico')),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro_contato',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade_endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cidade', models.ForeignKey(to='bussola.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Comenta_sobre_est',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario_estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comenta_est', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario_servico',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comenta_ser', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario_sobre_ser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comentario_servico', models.ForeignKey(to='bussola.Comentario_servico')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('complemento', models.CharField(max_length=45)),
                ('bairro', models.CharField(max_length=45)),
                ('numero', models.IntegerField()),
                ('rua', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimeto',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Fale_conosco',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Faz_comentario_est',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comentario_estabelecimento', models.ForeignKey(to='bussola.Comentario_estabelecimento')),
                ('endereco', models.ForeignKey(to='bussola.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Faz_comentario_ser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('comentario_servico', models.ForeignKey(to='bussola.Comentario_servico')),
                ('endereco', models.ForeignKey(to='bussola.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descricao_imagem', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Realiza_avaliacao_est',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('avaliacao_estabelecimento', models.ForeignKey(to='bussola.Avaliacao_estabelecimento')),
                ('endereco', models.ForeignKey(to='bussola.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Realiza_avaliacao_ser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('avaliacao_servico', models.ForeignKey(to='bussola.Avaliacao_servico')),
                ('endereco', models.ForeignKey(to='bussola.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(max_length=45)),
                ('informacoes_adicionais', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Servico_sub_categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('servico', models.ForeignKey(to='bussola.Servico')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_contato',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('tipo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cpf_cnpj', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_cadastra_ser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('servico', models.ForeignKey(to='bussola.Servico')),
                ('usuario', models.ForeignKey(to='bussola.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cidade', models.ForeignKey(to='bussola.Cidade')),
                ('endereco', models.ForeignKey(to='bussola.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_cria_notificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('notificacao', models.ForeignKey(to='bussola.Notificacao')),
                ('usuario', models.ForeignKey(to='bussola.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_le_notificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('notificacao', models.ForeignKey(to='bussola.Notificacao')),
                ('usuario', models.ForeignKey(to='bussola.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_segue_ser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('servico', models.ForeignKey(to='bussola.Servico')),
                ('usuario', models.ForeignKey(to='bussola.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='servico_sub_categoria',
            name='sub_categoria',
            field=models.ForeignKey(to='bussola.Sub_categoria'),
        ),
        migrations.AddField(
            model_name='imagens',
            name='servico',
            field=models.ForeignKey(to='bussola.Servico'),
        ),
        migrations.AddField(
            model_name='contato',
            name='tipo_contato',
            field=models.ForeignKey(to='bussola.Tipo_contato'),
        ),
        migrations.AddField(
            model_name='comentario_sobre_ser',
            name='servico',
            field=models.ForeignKey(to='bussola.Servico'),
        ),
        migrations.AddField(
            model_name='comenta_sobre_est',
            name='comentario_estabelecimento',
            field=models.ForeignKey(to='bussola.Comentario_estabelecimento'),
        ),
        migrations.AddField(
            model_name='comenta_sobre_est',
            name='endereco',
            field=models.ForeignKey(to='bussola.Endereco'),
        ),
        migrations.AddField(
            model_name='cidade_endereco',
            name='endereco',
            field=models.ForeignKey(to='bussola.Endereco'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='sub_categoria',
            field=models.ForeignKey(to='bussola.Sub_categoria'),
        ),
        migrations.AddField(
            model_name='cadastro_contato',
            name='contato',
            field=models.ForeignKey(to='bussola.Contato'),
        ),
        migrations.AddField(
            model_name='cadastro_contato',
            name='endereco',
            field=models.ForeignKey(to='bussola.Endereco'),
        ),
        migrations.AddField(
            model_name='avaliacao_sobre_ser',
            name='servico',
            field=models.ForeignKey(to='bussola.Servico'),
        ),
        migrations.AddField(
            model_name='avalia_local',
            name='avaliacao_estabelecimento',
            field=models.ForeignKey(to='bussola.Avaliacao_estabelecimento'),
        ),
        migrations.AddField(
            model_name='avalia_local',
            name='endereco',
            field=models.ForeignKey(to='bussola.Endereco'),
        ),
    ]
