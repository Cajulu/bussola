# -*- codinng: utf-8 -*-  
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
 
#Neste documento são feitos os forms que serão chamados pelos htmls

class UsuarioCadastroForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('cpfCnpj',)		
		widgets = {
			'cpfCnpj': forms.TextInput(attrs={'class': 'form-control','placeholder':'CPF ou CNPJ', 'name':'cpfCnpj', 'id':'cpfCnpj', 'maxlength':255}),
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
		
class UsuarioLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nome', 'name':'username', 'id':'username', 'maxlength':255}),
			'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Senha', 'name':'password', 'id':'password', 'maxlength':255}),
		}

class CadastroServicoForm(forms.ModelForm):
	class Meta:
		model = Servico
		fields = ['nomeServico', 'informacoesServico', 'informacoesPreco', 'categoria']

		widgets = {
			'nomeServico': forms.TextInput(attrs={'class': 'form-pesquisa', 'placeholder':'Nome do serviço', 'name':'nomeServico', 'id':'nomeServico','maxlength':255}),
			'informacoesServico': forms.TextInput(attrs={'class': 'form-pesquisa', 'placeholder':'Informações do Serviço', 'name':'informacoesServico', 'id':'informacoesServico','maxlength':255}),
			'informacoesPreco': forms.TextInput(attrs={'class': 'form-pesquisa', 'placeholder':'Informações de Preço', 'name':'informacoesPreco', 'id':'informacoesPreco','maxlength':255}),
			'categoria': forms.Select(attrs={'id':'id-categoria','class':'selectField'})
		}

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['tipo', 'descricaoContato']
        widgets = {
            'tipo': forms.Select(attrs={'id':'id-tipoContato','class':'selectField'}),
            'descricaoContato': forms.TextInput(attrs={'placeholder':'Descrição', 'name':'descricaoContato', 'id':'descricaoContato','maxlength':255}),
            }

class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = ['numero','cidade']

		widgets = {
		'numero': forms.TextInput(attrs={'placeholder':'Número', 'name':'numero', 'id':'numero'}),
		'cidade': forms.Select(attrs={'id':'id-cidade','class':'selectField'}),
		}

class RuaForm(forms.ModelForm):
	class Meta:
		model = Rua
		fields = ['rua']

		widgets = {
		'rua': forms.TextInput(attrs={'placeholder':'Rua', 'name':'rua', 'id':'rua','maxlength':255}),
		}

class BairroForm(forms.ModelForm):
	class Meta:
		model = Bairro
		fields = ['bairro']

		widgets = {
		'bairro': forms.TextInput(attrs={'placeholder':'Bairro', 'name':'bairro', 'id':'bairro','maxlength':255}),
		}

class PesquisaForm(forms.Form):
    servico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-pesquisa', 'placeholder':'Que serviço precisa?', 'name':'servico', 'id':'servico','maxlength':255}))

class SenhaForm(forms.Form):
	senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-pesquisa', 'name':'senha', 'id':'senha','maxlength':255}))

class ImagemForm(forms.ModelForm):

	class Meta:
		model = Imagens
		fields = ['descricaoImagem']