from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/', views.do_login, name="login"),
    url(r'^logout/', views.do_logout, name='logout'),
    url(r'^cadastro/', views.cadastro, name="cadastro"),
    url(r'^recuperacao_senha/', views.recuperacao_senha, name="recuperacao_senha"),
    url(r'^servico/', views.servico, name="servico"),
    url(r'^cadastro_servico/', views.cadastro_servico, name="cadastro_servico"),
    url(r'^pagina_usuario/', views.pagina_usuario, name="pagina_usuario"),
    url(r'^meu_servico/', views.meu_servico, name="meu_servico"),
    url(r'^meu_servico_cadastro/', views.meu_servico_cadastro, name="meu_servico_cadastro"),
    url(r'^servico_login/', views.servico_login, name="servico_login"),
    url(r'^alterar_servico/', views.alterar_servico, name="alterar_servico"),
    url(r'^lista_servicos/', views.lista_servicos, name="lista_servicos"),

]