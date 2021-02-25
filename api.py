#Importing Libary
import requests
import json
from json import JSONEncoder
from bs4 import BeautifulSoup
from datetime import datetime
import re
import connexion
from googlesearch import search
from facebook_scraper import get_posts

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import os, sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugin-port=9222")
options.add_argument("--screen-size=1200x800")
options.add_argument("--disable-popup-blocking")
options.add_argument("test-type")
#options.add_argument('--headless')


def stf(nome):
    global driver_stf
    driver_stf = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=options.to_capabilities())
    driver_stf.implicitly_wait(1)
    stf_url = 'http://portal.stf.jus.br/processos/listarPartes.asp?termo='
    driver_stf.get(stf_url + nome)
    sleep(3)
    quantidade = driver_stf.find_element_by_xpath('//*[@id="quantidade"]').text
    result = str(quantidade)
    driver_stf.quit()
    return "Quantidade de Processos: " + result

def jusbrasil(nome):
    global driver_jb
    driver_jb = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=options.to_capabilities())
    driver_jb.implicitly_wait(1)
    jb_url = 'https://www.jusbrasil.com.br/consulta-processual/busca?q='
    driver_jb.get(jb_url + nome)
    sleep(3)
    jusbrasil = driver_jb.find_elements_by_xpath('//*[@id="app-root"]/div/div/div[1]/div[2]/div[2]')
    if len(jusbrasil) > 0:
        jusbrasil = driver_jb.find_element_by_xpath('//*[@id="app-root"]/div/div/div[1]/div[2]/div[2]')
        result = jusbrasil.text.replace("\n"," | ")
        driver_jb.quit()
        return result
    else:
        return "Não possui processos registrados."

def google(nome):
    data = []
    for url in search(nome, num_results=5):
        data.append(url)
    return data

def facebook(nome):
    #data = []
    #for post in get_posts(nome, pages=1):
    #    data.append(post['text'][:50])
    return nome + " not checked on Facebook"

#Function calls	
def check(nome):
    Google = google(nome)
    Stf = stf(nome)
    Jusbrasil = jusbrasil(nome)
    Facebook = facebook(nome)

    obj = {
        "data" : {
            "Google" : Google,
            "Facebook" : Facebook,
            "STF" : Stf,
            "Jusbrasil" : Jusbrasil,
            "Data de Procura" : datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        },
        "error" : []
    }
    return obj, 200