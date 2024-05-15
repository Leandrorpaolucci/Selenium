#Autor: Leandro Ribeiro

from time import sleep
from features.support.ambiente import * # type: ignore
from features.support.elements import * # type: ignore
from features.support.page_utils import PageUtils # type: ignore
from features.support.message import *

page_utils = PageUtils()

class PesquisaTemperatura:
    def acessar_site_google(context):
        page_utils.open_browser(URL_GOOGLE) # type: ignore
        
    def pesquisar_temperatura_caixa_google(context):
        page_utils.clicar_elemento_pagina(CAIXA_PESQUISA_GOOGLE)
       

    def inserir_texto_no_elemento(context):
        page_utils.inserir_dados_no_elemento(CAIXA_PESQUISA_GOOGLE, DESCRICAO_PESQUISA)
        

    def click(context):
        page_utils.clicar_elemento_pagina(BTN_DESCRICAO_PESQUISA)
        sleep(10)
