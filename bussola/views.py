from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from bussola.models import Usuario
from django.contrib.auth.models import User

def index(request):
	return render(request, 'index.html', {})

def do_login(request):
    formLogin = UsuarioLoginForm()
    if request.method == 'POST':
        user=authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/pagina_usuario/')
    return render(request, 'login.html', {'formLogin':formLogin })

def do_logout(request):
    logout(request)
    return render('/index/')


def cadastro(request):
    if request.method == 'POST':
        formUsuario = UsuarioCadastroForm(request.POST, request.FILES)
        formUser = UserCadastroForm(request.POST)
        if formUser.is_valid() and formUsuario.is_valid():
            cpf_cnpj = formUsuario.cleaned_data['cpf_cnpj']
            username = formUser.cleaned_data['username']
            email = formUser.cleaned_data['email']
            password = formUser.cleaned_data['password']
            user = User.objects.create_user(username, email, password )
            user.save()

            usuario = Usuario.objects.create(user=user, cpf_cnpj=cpf_cnpj)
            usuario.save()
            
            return redirect('/login/')
    else:
        formUsuario = UsuarioCadastroForm()
        formUser = UserCadastroForm()

    return render(request, 'cadastro.html', {'formUsuario':formUsuario, 'formUser':formUser})

#terminar de adicionar os atributos e resolver o problema das chamadas ods forms  
def cadastro_servico(request):
    if request.method == 'POST':
        formCadastroServico = CadastroServico(request.POST)
        if formCadastroServico.is_valid():
            nome_servico = formCadastroServico.cleaned_data['nome_servico']
            informacoes_servico = formCadastroServico.cleaned_data['infomacoes_servico'] 
            informacoes_preco = formCadastroServico.cleaned_data['infomacoes_preco'] 
            outros = formCadastroServico.cleaned_data['outros']

            servico = Servico.objects.create( nome_servico=nome_servico, infomacoes_servico=infomacoes_servico, infomacoes_preco=informacoes_preco, outros=outros)
            servico.save()
            return redirect('/meu_servico/')
    else:
        formCadastroServico = CadastroServico(request.POST)
    
    return render(request, 'cadastro_servico.html', {'formCadastroServico':formCadastroServico})


def recuperacao_senha(request):
    return render(request, 'recuperacao_senha.html', {})
   

def meu_servico(request):
    return render(request, 'meu_servico.html', {})

def servico(request):
    return render(request, 'servico.html', {})

def pagina_usuario(request):
    return render(request, 'pagina_usuario.html', {})

def meu_servico_cadastro(request):
    return render(request, 'meu_servico_cadastro.html', {})

def servico_login(request):
    return render(request, 'servico_login.html', {})

def alterar_servico(request):
    return render(request, 'alterar_servico.html', {})

def lista_servicos(request):
    return render(request, 'lista_servicos.html', {})



