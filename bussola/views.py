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
    if request.method == 'POST':
        formPesquisa = PesquisaForm(request.POST)
        
        if formPesquisa.is_valid():
            servico = formPesquisa.cleaned_data['servico']
            servicoPesquisado = Servico.objects.filter(nomeServico=servico)
            return redirect('/lista_pesquisa_servico/', {'servicoPesquisado':servicoPesquisado})
    
    else:
        formPesquisa = PesquisaForm()
        
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias':categorias, 'formPesquisa':formPesquisa})

def listaPesquisaServico(request):
    servicos = Servico.objects.all()
    return render(request, 'lista_pesquisa_servico.html', {'servicos': servicos})
 
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
        
        formContato = ContatoForm(request.POST)

        formRua = RuaForm(request.POST)

        formBairro =BairroForm(request.POST)
    
        if formCadastroServico.is_valid () and formContato.is_valid() and formEndereco.is_valid() and formImagem.is_valid() and formRua.is_valid() and formBairro.is_valid():
            
            #certo!
            nomeServico = formCadastroServico.cleaned_data['nomeServico']
            informacoesServico = formCadastroServico.cleaned_data['informacoesServico'] 
            informacoesPreco = formCadastroServico.cleaned_data['informacoesPreco']

            categoria = formCadastroServico.cleaned_data['categoria']
            categoriaAux = Categoria.objects.get(pk=categoria.pk)

            servico = Servico.objects.create( nomeServico=nomeServico, informacoesServico=informacoesServico, informacoesPreco=informacoesPreco, categoria=categoriaAux, usuario=usuario)
            servico.save()

            descricaoImagem = formImagem.cleaned_data['descricaoImagem']

            imagem = Imagens.objects.create(descricaoImagem=descricaoImagem, servico=servico)
            imagem.save()
        
            #certo!

            cidade = formEndereco.cleaned_data['cidade']
            cidadeAux = Cidade.objects.get(pk=cidade.pk)
            
            nomeBairro = formBairro.cleaned_data['bairro']
            bairro = Bairro.objects.create(bairro=nomeBairro)
            bairro.save()

            numero = formEndereco.cleaned_data['numero']
            
            nomeRua = formRua.cleaned_data['rua']
            rua = Rua.objects.create(rua=nomeRua)
            rua.save()

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
        formContato = ContatoForm()
        formRua = RuaForm()
        formBairro =BairroForm()
       

    return render(request, 'cadastro_servico.html', {'formCadastroServico':formCadastroServico,  'formContato':formContato, 'formEndereco':formEndereco,'formImagem':formImagem, 'formRua':formRua, 'formBairro':formBairro})

def recuperacaoSenha(request):
    return render(request, 'recuperacao_senha.html', {})

@login_required
def paginaUsuario(request):
    
    if request.method == 'POST':
        formPesquisa = PesquisaForm(request.POST)
        
        if formPesquisa.is_valid():
            servico = formPesquisa.cleaned_data['servico']
            servicoPesquisado = Servico.objects.filter(nomeServico=servico)
            return redirect('/lista_pesquisa_servico/', {'servicoPesquisado':servicoPesquisado})
    
    else:
        formPesquisa = PesquisaForm()
        
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias':categorias, 'formPesquisa':formPesquisa})


def novaSenha(request):

    formUsu = UserCadastroForm(request.POST) 
    formSenha = SenhaForm(request.POST)

    if request.method == 'POST':
        print(request)
        if formUsu.is_valid() and formSenha.is_valid():
            nome = formUsu.cleaned_data['username']
            senha = formSenha.cleaned_data['senha']
            novaSenha = formUsu.cleaned_data['password']
            filtro = User.objects.get(username=nome, password=senha)
            filtro.password = novaSenha
            filtro.save()
        
            return redirect('/login/')

        else:
            formUsu = UserCadastroForm()
            formSenha = SenhaForm()

    return render(request, 'recuperacao_senha.html', {'formUsu':formUsu, 'formSenha': formSenha})

@login_required
def listaMeuServico(request):
    user = request.user
    usuario = Usuario.objects.get(user=user)
    servicos = Servico.objects.filter(usuario=usuario)
    return render(request, 'lista_meu_servico.html', {'servicos': servicos})

@login_required
def meuServico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    endereco = Endereco.objects.get(servico=servico)
    contato = Contato.objects.get(servico = servico)
    imagem = Imagens.objects.get(servico=servico)
    return render(request, 'meu_servico.html', {'servico': servico, 'endereco':endereco, 'contato':contato, 'imagem':imagem})

@login_required
def alterarServico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)

    user = request.user
    usuario = Usuario.objects.get(user=user.pk)

    if request.method == 'POST':

        formCadastroServico = CadastroServicoForm(request.POST, request.FILES, instance=servico)
        
        formEndereco = EnderecoForm(request.POST, instance=servico)

        formImagem = ImagemForm(request.POST, request.FILES, instance=servico)
        
        
        formContato = ContatoForm(request.POST, instance=servico)
        
        formRua = RuaForm(request.POST)

        formBairro =BairroForm(request.POST)
        


        if formCadastroServico.is_valid () and formContato.is_valid() and formEndereco.is_valid() and formImagem.is_valid() and formRua.is_valid() and formBairro.is_valid():
            
            #certo!
            formCadastroServico.save() 
        
            formEndereco.save() 
            formImagem.save()     
            
            formContato.save() 
            
            formRua.save()

            formBairro.save()
        
           
                
            return redirect('/lista_meu_servico/')
    
    else:
        formCadastroServico = CadastroServicoForm(instance=servico)
        formEndereco = EnderecoForm(instance=servico)
        formImagem = ImagemForm(instance=servico)
       
        formContato = ContatoForm(instance=servico)
        formRua = RuaForm()
        formBairro =BairroForm()
        
        

    return render(request, 'alterar_servico.html', {'formCadastroServico':formCadastroServico, 'formContato':formContato,'formEndereco':formEndereco, 'formImagem':formImagem, 'formRua':formRua, 'formBairro':formBairro})

    """
    formCadastroServico = CadastroServicoForm(request.POST, request.FILES, instance=servico)
        
    formEndereco = EnderecoForm(request.POST or None, instance=servico)

    formImagem = ImagemForm(request.POST, request.FILES, instance=servico)
    
    formCidade = CidadeForm(request.POST or None)
    
    formContato = ContatoForm(request.POST or None, instance=servico)
    
    formTipoContato = TipoContatoForm(request.POST or None)
    
    formCategoria = CategoriaForm(request.POST or None)

    formRua = RuaForm(request.POST or None)

    formBairro = BairroForm(request.POST or None)
    
    if formCadastroServico.is_valid():
        formCadastroServico.save() 
        
        formEndereco.save() 
        formImagem.save()     
        formCidade.save() 
        formContato.save() 
        formTipoContato.save() 
        formCategoria.save()
        formRua.save() 
        formBairro.save() 
    
        return redirect('/meu_servico/')

    return render(request, 'cadastro_servico.html', {'formCadastroServico':formCadastroServico})
    """
def categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    servicos = Servico.objects.filter(categoria=categoria)
    return render(request, 'lista_servicos.html', {'servicos': servicos})

def servico(request, pk):
    servico = Servico.objects.get(pk=pk)
    endereco = Endereco.objects.get(servico=servico)
    contato = Contato.objects.get(servico = servico)
    imagem = Imagens.objects.get(servico=servico)
    return render(request, 'servico.html', {'servico': servico, 'endereco':endereco, 'contato':contato, 'imagem':imagem})

#https://rayed.com/wordpress/?p=1266

def deletarServico(request, pk):
    objeto = get_object_or_404(Servico, pk=pk)
    print(objeto)
    objeto.delete()
    return redirect('/lista_meu_servico/')
