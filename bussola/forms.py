# -*- codinng: utf-8 -*- 
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User


#Neste documento são feitos os forms que serão chamados pelos htmls

class UsuarioCadastroForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('cpf_cnpj',)		
		widgets = {
			'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control','placeholder':'CPF ou CNPJ', 'name':'cpf_cnpj', 'id':'cpj_cnpj', 'maxlength':255}),
		}



class UserCadastroForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password', 'username',)
		
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nome', 'name':'username', 'id':'username', 'maxlength':255}),
			'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email', 'name':'email', 'id':'email', 'maxlength':255}),
			'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Senha', 'name':'password', 'id':'password', 'maxlength':255}),
			
		}
		
	#salva no BD
	
	def save(self, commit=True):
		user = super(UsuarioCadastroForm, self).save(commit=False)
		user.set_password()
		if commit:
			user.save()

		return user

class UsuarioLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome', 'name':'username', 'id':'username', 'maxlength':255}),
			'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Senha', 'name':'password', 'id':'password', 'maxlength':255}),
		}

class CadastroServico(forms.ModelForm):
	class Meta:
		model = Servico
		fields = ('nome_servico', 'informacoes_servico', 'informacoes_preco')

		widgets = {
			'nome_servico': forms.TextInput(attrs={'class': 'form-pesquisa', 'placeholder':'Nome do serviço', 'name':'nome_servico', 'id':'nome_servico','maxlength':255}),
			'informacoes_servico': forms.TextInput(attrs={'class': 'form-pesquisa', 'placeholder':'Informações do Serviço', 'name':'informacoes_servico', 'id':'informacoes_servico','maxlength':255}),
			'informacoes_preco': forms.TextInput(attrs={'class': 'form-pesquisa', 'placeholder':'Informações de Preço', 'name':'informacoes_preco', 'id':'informacoes_preco','maxlength':255}),
		}

	def saveServico(self, commit=True):
		servico = super(CadastroServico, self).save(commit=False)
		servico.set_password()
		if commit:
			servico.save()

		return servico


class NotificacaoForm(forms.ModelForm):

	class Meta:
		model = Notificacao
		fields = ('descricao',)

class CidadeForm(forms.ModelForm):

	class Meta:
		model = Cidade
		fields = ('descricao',)

class ServicoForm(forms.ModelForm):

	class Meta:
		model = Servico
		fields = '__all__'

class Sub_categoriaForm(forms.ModelForm):

	class Meta:
		model = Sub_categoria
		fields = ('descricao',)

class Comentario_servicoForm(forms.ModelForm):

	class Meta:
		model = Comentario_servico
		fields = '__all__'

class Tipo_contatoForm(forms.ModelForm):

	class Meta:
		model = Tipo_contato
		fields = ('tipo',)

class ContatoForm(forms.ModelForm):

	class Meta:
		model = Contato
		fields = '__all__'

class Avaliacao_servicoForm(forms.ModelForm):

	class Meta:
		model = Avaliacao_servico
		fields = ('numero_estrelas_ser',)

class CategoriaForm(forms.ModelForm):

	class Meta:
		model = Categoria
		fields = '__all__'

class EstabelecimetoForm(forms.ModelForm):

	class Meta:
		model = Estabelecimeto
		fields = ('nome',)

class EnderecoForm(forms.ModelForm):

	class Meta:
		model = Endereco
		fields = '__all__'

class Avaliacao_estabelecimentoForm(forms.ModelForm):

	class Meta:
		model = Avaliacao_estabelecimento
		fields = ('numero_estrelas_est',)

class Comentario_estabelecimentoForm(forms.ModelForm):

	class Meta:
		model = Comentario_estabelecimento
		fields = ('comenta_est',)

class ImagemForm(forms.ModelForm):

	class Meta:
		model = Imagens
		fields = '__all__'

class Fale_conoscoForm(forms.ModelForm):

	class Meta:
		model = Fale_conosco
		fields = '__all__'