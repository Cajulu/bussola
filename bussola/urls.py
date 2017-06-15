from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/', views.do_login, name="login"),
    url(r'^cadastro/', views.cadastro, name="cadastro"),
    url(r'^recuperacao_senha/', views.recuperacaoSenha, name="recuperacao_senha"),
    url(r'^servico/', views.servico, name="servico"),
    url(r'^cadastro_servico/', views.cadastroServico, name="cadastro_servico"),
    url(r'^pagina_usuario/', views.paginaUsuario, name="pagina_usuario"),
    url(r'^meu_servico/', views.meuServico, name="meu_servico"),
    url(r'^lista_meu_servico/', views.listaMeuServico, name="lista_meu_servico"),
    url(r'^servico_login/', views.servicoLogin, name="servico_login"),
    url(r'^alterar_servico/', views.alterarServico, name="alterar_servico"),
    url(r'^lista_servicos/', views.listaServicos, name="lista_servicos"),
]