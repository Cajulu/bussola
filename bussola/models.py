from django.db import models
from django.contrib.auth.models import User

class Notificacao(models.Model):
	descricao = models.CharField(max_length=200)

	def __str__(self):
		return self.descricao
	
class Cidade(models.Model):
	descricao = models.CharField(max_length=200)

	def __str__(self):
		return self.descricao

class Servico(models.Model):
	nome_servico = models.CharField(max_length=45)
	informacoes_servico = models.CharField(max_length=200)
	informacoes_preco = models.CharField(max_length=200)

	def __str__(self):
		return self.nome_servico

#ALIMENTACAO = (('laches',u'Lanches'),('tapioca',u'Tapioca'))
#REFORMAS_REPAROS = (('construcao',u'Construcao'),('pinturas',u'Pinturas'))
class Sub_categoria(models.Model):
	descricao = models.CharField(max_length=200)
	
	

	def __str__(self):
		return self.descricao


class Comentario_servico(models.Model):
	comenta_ser =  models.CharField(max_length=200)

	def __str__(self):
		return self.comenta_ser

class Tipo_contato(models.Model):
	tipo = models.CharField(max_length=45)

	def __str__(self):
		return self.tipo


class Contato(models.Model):
	tipo_contato = models.ForeignKey(Tipo_contato)
	descricao = models.CharField(max_length=45)
	
	def __str__(self):
		return self.descricao

class Avaliacao_servico(models.Model):
	numero_estrelas_ser = models.IntegerField()

	def __str__(self):
		return self.numero_estrelas_ser


class Categoria(models.Model):
	sub_categoria = models.ForeignKey(Sub_categoria)
	#alimentacao = models.CharField(max_length=16, choices=ALIMENTACAO)
	#reformas_reparos = models.CharField(max_length=16, choices=REFORMAS_REPAROS)
	

	def __str__(self):
		return self.descricao

class Estabelecimeto(models.Model):
	nome = models.CharField(max_length=45)

	def __str__(self):
		return self.nome

class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cpf_cnpj = models.IntegerField()
	 
	def __str__(self):
		return self.user.username

class Endereco (models.Model):
	bairro = models.CharField(max_length=45)
	numero  = models.IntegerField()
	rua = models.CharField(max_length=45)
	complemento = models.CharField(max_length=45)
	
	def __str__(self):
		return self.bairro

class Avaliacao_estabelecimento(models.Model):
	numero_estrelas_est = models.IntegerField()

	def __str__(self):
		return self.numero_estrelas_est

class Comentario_estabelecimento(models.Model):
	comenta_est =  models.CharField(max_length=200)

	def __str__(self):
		return self.comenta_est

class Imagens(models.Model):
	servico = models.ForeignKey(Servico)
	descricao_imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

	def __str__(self):
		return self.descricao_imagem


class Fale_conosco(models.Model):
	email = models.EmailField(max_length=254)
	mensagem = models.CharField(max_length=200)

	def __str__ (self):
		return self.email

class Usuario_le_notificacao(models.Model):
	notificacao = models.ForeignKey(Notificacao)
	usuario = models.ForeignKey(Usuario)

class Usuario_segue_ser(models.Model):
	usuario = models.ForeignKey(Usuario)
	servico = models.ForeignKey(Servico)

class Usuario_cadastra_ser(models.Model):
	usuario = models.ForeignKey(Usuario)
	servico = models.ForeignKey(Servico)

class Usuario_cria_notificacao(models.Model):
	notificacao = models.ForeignKey(Notificacao)
	usuario = models.ForeignKey(Usuario)

class Cadastro_contato(models.Model):
	contato = models.ForeignKey(Contato)
	endereco = models.ForeignKey(Endereco)

class Realiza_avaliacao_ser(models.Model):
	endereco = models.ForeignKey(Endereco)
	avaliacao_servico = models.ForeignKey(Avaliacao_servico)

class Faz_comentario_ser(models.Model):
	endereco = models.ForeignKey(Endereco)
	comentario_servico = models.ForeignKey(Comentario_servico)

class Comentario_sobre_ser(models.Model):
	servico = models.ForeignKey(Servico)
	comentario_servico = models.ForeignKey(Comentario_servico)

class Avaliacao_sobre_ser(models.Model):
	servico = models.ForeignKey(Servico)
	avaliacao_servico = models.ForeignKey(Avaliacao_servico)

class Cidade_endereco(models.Model):
	endereco = models.ForeignKey(Endereco)
	cidade = models.ForeignKey(Cidade)

class Servico_sub_categoria(models.Model):
	servico = models.ForeignKey(Servico)
	sub_categoria = models.ForeignKey(Sub_categoria)

class Comenta_sobre_est(models.Model):
	endereco = models.ForeignKey(Endereco)
	comentario_estabelecimento = models.ForeignKey(Comentario_estabelecimento)

class Faz_comentario_est(models.Model):
	comentario_estabelecimento = models.ForeignKey(Comentario_estabelecimento)
	endereco = models.ForeignKey(Endereco)

class Realiza_avaliacao_est(models.Model):
	endereco = models.ForeignKey(Endereco)
	avaliacao_estabelecimento = models.ForeignKey(Avaliacao_estabelecimento)

class Avalia_local(models.Model):
	endereco = models.ForeignKey(Endereco)
	avaliacao_estabelecimento = models.ForeignKey(Avaliacao_estabelecimento)

class Usuario_cidade(models.Model):
	endereco = models.ForeignKey(Endereco)
	cidade = models.ForeignKey(Cidade)