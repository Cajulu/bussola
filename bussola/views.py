from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from bussola.models import Usuario
from django.contrib.auth.models import User 
import json
from django.http import HttpResponse
 
def index(request):
    """if request.method == 'POST':
        formPesquisa = PesquisaForm(request.POST)

        if formPesquisa.is_valid():
            pesquisaServico = formPequisa.cleaned_data['pesquisaServico']
            pesquisaRegiao = formPesquisa.cleaned_data['pesquisaRegiao']

            #FAZER O SELECT

            return render(request, 'index.html', {})

    else:
        formPesquisa = PesquisaForm()"""

    return render(request, 'index.html')

	
 
def do_login(request):
    formLogin = UsuarioLoginForm()
    if request.method == 'POST':
        user=authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/pagina_usuario/')
    return render(request, 'login.html', {'formLogin':formLogin })


def cadastro(request):
    if request.method == 'POST':
        formUsuario = UsuarioCadastroForm(request.POST)
        formUser = UserCadastroForm(request.POST)
        if formUser.is_valid() and formUsuario.is_valid():
            cpfCnpj = formUsuario.cleaned_data['cpfCnpj']
            username = formUser.cleaned_data['username']
            email = formUser.cleaned_data['email']
            password = formUser.cleaned_data['password']
            user = User.objects.create_user(username, email, password )
            user.save()

            usuario = Usuario.objects.create(user=user, cpfCnpj=cpfCnpj)
            usuario.save()
            
            return redirect('/login/')
    else:
        formUsuario = UsuarioCadastroForm()
        formUser = UserCadastroForm()

    return render(request, 'cadastro.html', {'formUsuario':formUsuario, 'formUser':formUser})

#terminar de adicionar os atributos e resolver o problema das chamadas ods forms  

@login_required
def cadastroServico(request):
    
    user = request.user
    usuario = Usuario.objects.get(user=user.pk)

    if request.method == 'POST':

        formCadastroServico = CadastroServicoForm(request.POST, request.FILES)
        
        formEndereco = EnderecoForm(request.POST)

        formImagem = ImagemForm(request.POST, request.FILES )
        
        formCidade = CidadeForm(request.POST)
        
        formContato = ContatoForm(request.POST)
        
        formTipoContato = TipoContatoForm(request.POST)
        
        formCategoria = CategoriaForm(request.POST)

        formRua = RuaForm(request.POST)

        formBairro = BairroForm(request.POST)


        
        if formCadastroServico.is_valid () and formCategoria.is_valid() and formContato.is_valid() and formTipoContato.is_valid() and formEndereco.is_valid() and formCidade.is_valid() and formImagem.is_valid() and formRua.is_valid() and formBairro.is_valid():
            
            #certo!
            nomeServico = formCadastroServico.cleaned_data['nomeServico']
            informacoesServico = formCadastroServico.cleaned_data['informacoesServico'] 
            informacoesPreco = formCadastroServico.cleaned_data['informacoesPreco']

            categoria = formCadastroServico.cleaned_data['categoria']
            categoriaAux = Categoria.objects.get(pk=categoria.pk)

            servico = Servico.objects.create( nomeServico=nomeServico, informacoesServico=informacoesServico, informacoesPreco=informacoesPreco, categoria=categoriaAux, usuario=usuario)
            servico.save()

            descricaoImagem = formImagem.cleaned_data['descricaoImagem']
            #nome = formImagem.cleaned_data['nome']
            imagem = Imagens.objects.create(descricaoImagem=descricaoImagem, servico=servico)
            imagem.save()
        
            #imagem = formImagem.cleaned_data['imagem']
            #certo!
            nomeBairro = formBairro.cleaned_data['bairro']
            bairro = Bairro.objects.create(bairro=nomeBairro)
            bairro.save()

            numero = formEndereco.cleaned_data['numero']
            
            nomeRua = formRua.cleaned_data['rua']
            rua = Rua.objects.create(rua=nomeRua)
            rua.save()

            cidade = formEndereco.cleaned_data['cidade']
            cidadeAux = Cidade.objects.get(pk=cidade.pk)

            endereco = Endereco.objects.create(bairro=bairro, numero=numero, rua=rua, cidade=cidadeAux, servico=servico)
            endereco.save()

            tipo = formContato.cleaned_data['tipo']
            descricaoContato = formContato.cleaned_data['descricaoContato']
            tipoContato = TipoContato.objects.get(pk=tipo.pk)
            
            contato = Contato.objects.create(tipo=tipoContato, descricaoContato=descricaoContato, servico=servico)
            contato.save()

            
            return redirect('/lista_meu_servico/')
    else:
        formCadastroServico = CadastroServicoForm()
        formEndereco = EnderecoForm()
        formImagem = ImagemForm()
        formCidade = CidadeForm()
        formContato = ContatoForm()
        formTipoContato = TipoContatoForm()
        formCategoria = CategoriaForm()
        formBairro = BairroForm()
        formRua = RuaForm()

    return render(request, 'cadastro_servico.html', {'formCadastroServico':formCadastroServico, 'formCategoria':formCategoria, 'formContato':formContato, 'formTipoContato':formTipoContato, 'formEndereco':formEndereco, 'formCidade':formCidade, 'formImagem':formImagem, 'formRua':formRua, 'formBairro':formBairro})

def recuperacaoSenha(request):
    return render(request, 'recuperacao_senha.html', {})

@login_required
def paginaUsuario(request):
    """ if request.method == 'POST':
        formPesquisa = PesquisaForm(request.POST)

        if formPesquisa.is_valid():
            pesquisaServico = formPequisa.cleaned_data['pesquisaServico']
            pesquisaRegiao = formPesquisa.cleaned_data['pesquisaCidade']



            #FAZER O SELECT

            return render(request, 'pagina_usuario.html', {'formPesquisa':formPesquisa})

    else:
        formPesquisa = PesquisaForm()"""
    return render(request, 'pagina_usuario.html')


@login_required
def listaMeuServico(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    servico = Servico.objects.all().filter(usuario=usuario)
    return render(request, 'lista_meu_servico.html', {'servico': servico})

@login_required
def meuServico(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    servico = Servico.objects.all().filter(usuario=usuario)
    return render(request, 'meu_servico.html', {})

@login_required
def alterarServico(request):
    return render(request, 'alterar_servico.html', {})

def listaServicos(request):
    servico = Servico.objects.all().filter()
    return render(request, 'lista_servicos.html', {'servico': servico})

def servico(request):
    servico = Servico.objects.all().filter()
    return render(request, 'servico.html', {'servico': servico})
    
def servicoLogin(request):
    return render(request, 'servico_login.html', {})

