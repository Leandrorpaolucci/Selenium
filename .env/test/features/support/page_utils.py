#Autor: Leandro Ribeiro
import unittest, base64, time, os, subprocess, pytz, allure, json, urllib3, behave, behave_html_formatter

from behave import *
from selenium import webdriver
from ..support.ambiente import *


class PageUtils(unittest.TestCase):
    #Configurações e opções Microsoft Edge
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--disable-site-isolation-trials')
    edge_options.add_argument('--ignore-certificate-errors')
    edge_options.add_argument('--start-maximized')
    driver = webdriver.Edge(options=edge_options)
    
    
    def open_browser(context, url):
        context.driver.get(url)
        
    def clear_browser(context):
        context.driver.delete_all_cookies()
        
    def exit_browser(context):
        context.driver.quit()
    
    
