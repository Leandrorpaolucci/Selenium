#Autor: Leandro

from behave import *
from features.pages.consulta_temperatura_google_pages import PesquisaTemperatura # type: ignore

pesquisa_temperatura = PesquisaTemperatura

@given(u'que eu estou no site do google')
def step_impl(context):
    pesquisa_temperatura.acessar_site_google(context)

@when(u'eu pesquiso a temperatura de hoje')
def step_impl(context):
    pesquisa_temperatura.pesquisar_temperatura_caixa_google(context)
    pesquisa_temperatura.inserir_texto_no_elemento(context)
    pesquisa_temperatura.click(context)

@then(u'o navegador deve trazer a temperatura de hoje')
def step_impl(context):
    ...
   
@then(u'fecho o navegador')
def step_impl(context):
    ...