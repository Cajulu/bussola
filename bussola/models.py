from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cpfCnpj = models.IntegerField()
	 
	def __str__(self):
		return self.user.username
		
class Categoria(models.Model):
	categoria = models.CharField(max_length=200)

	def __str__(self):
		return self.categoria

class Cidade(models.Model):
	cidade  = models.CharField(max_length=200)

	def __str__(self):
		return self.cidade

class Servico(models.Model):
	nomeServico = models.CharField(max_length=200)
	informacoesServico = models.CharField(max_length=200)
	informacoesPreco = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria, null=True, blank=False, verbose_name='Categoria')
	usuario = models.ForeignKey(Usuario, null=True, blank=False, verbose_name='Usuario')

	def __str__(self):
		return self.nomeServico


class Endereco(models.Model):
	numero = models.IntegerField()	
	cidade = models.ForeignKey(Cidade, null=True, blank=False, verbose_name='Cidade')
	servico = models.ForeignKey(Servico, null=True, blank=False, verbose_name='Servico')

	def __str__(self):
		return self.cidade.cidade

class Rua(models.Model):
	rua = models.CharField(max_length=200)
	endereco = models.ForeignKey(Endereco, null=True, blank=False, verbose_name='Endereco')
	
	def __str__(self):
		return self.rua

class Bairro(models.Model):
	bairro = models.CharField(max_length=200)
	endereco = models.ForeignKey(Endereco, null=True, blank=False, verbose_name='Endereco')

	def __str__(self):
		return self.bairro


class Imagens(models.Model):
	descricaoImagem = models.ImageField(upload_to='fotos', null=True)
	servico = models.ForeignKey(Servico, null=True, blank=False, verbose_name='Servico')

	def __str__(self):
		return self.servico.nomeServico

class TipoContato(models.Model):
	tipo = models.CharField(max_length=200)

	def __str__(self):
		return self.tipo

class Contato(models.Model):
	descricaoContato = models.CharField(max_length=200)
	tipo = models.ForeignKey(TipoContato, null=True, blank=False, verbose_name='TipoContato')
	servico = models.ForeignKey(Servico, null=True, blank=False, verbose_name='Servico')

	def __str__(self):
		return self.descricaoContato

