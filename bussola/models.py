from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cpfCnpj = models.IntegerField()
	 
	def __str__(self):
		return self.user.username

class FaleConosco(models.Model):
	email = models.CharField(max_length=200)
	mensagem = models.CharField(max_length=200)

	def __str__(self):
		return self.email

class Comentario(models.Model):
	comentario = models.CharField(max_length=200)

	def __str__(self):
		return self.comentario

		
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
	cidade = models.ForeignKey(Cidade, null=True, blank=False, verbose_name='Cidade')
	categoria = models.ForeignKey(Categoria, null=True, blank=False, verbose_name='Categoria')
	usuario = models.ForeignKey(Usuario, null=True, blank=False, verbose_name='Usuario')

	def __str__(self):
		return self.nomeServico

class Avaliacao(models.Model):
	numeroEstrelas = models.IntegerField()

	def __str__(self):
		return self.numeroEstrelas

class Rua(models.Model):
	rua = models.CharField(max_length=200)

	def __str__(self):
		return self.rua

class Bairro(models.Model):
	bairro = models.CharField(max_length=200)

	def __str__(self):
		return self.bairro

class Endereco(models.Model):
	numero = models.IntegerField()
	bairro = models.ForeignKey(Bairro, null=True, blank=False, verbose_name='Bairro')
	rua = models.ForeignKey(Rua, null=True, blank=False, verbose_name='Rua')
	servico = models.ForeignKey(Servico, null=True, blank=False, verbose_name='Servico')

	def __str__(self):
		return self.cidade.cidade

class Imagens(models.Model):
	descricaoImagem = models.ImageField(upload_to="bussola/static/img")
	servico = models.ForeignKey(Servico, null=True, blank=False, verbose_name='Servico')

	def __str__(self):
		return self.servico.nomeServico

class Avalia(models.Model):
	servico = models.ForeignKey(Servico, null=True, blank=False, verbose_name='Servico')
	avaliacao = models.ForeignKey(Avaliacao, null=True, blank=False, verbose_name='Avaliacao')

	def __str__(self):
		return self.servico

class Comenta(models.Model):
	servico = models.ForeignKey(Servico, null=True, blank=False, verbose_name='Servico')
	comentario = models.ForeignKey(Comentario, null=True, blank=False, verbose_name='Comentario')

	def __str__(self):
		return self.comentario

class Realiza(models.Model):
	usuario = models.ForeignKey(Usuario, null=True, blank=False, verbose_name='Usuario')
	avaliacao = models.ForeignKey(Avaliacao, null=True, blank=False, verbose_name='Avaliacao')

	def __str__(self):
		return self.avaliacao

class FazComentario(models.Model):
	usuario = models.ForeignKey(Usuario, null=True, blank=False, verbose_name='Usuario')
	comentario = models.ForeignKey(Comentario, null=True, blank=False, verbose_name='Comentario')

	def __str__(self):
		return self.comentario

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