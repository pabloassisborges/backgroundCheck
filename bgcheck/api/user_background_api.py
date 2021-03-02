from random import randint
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from bgcheck.services import web_search_service


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugin-port=9222")
options.add_argument("--screen-size=1200x800")
options.add_argument("--disable-popup-blocking")
options.add_argument("test-type")


def stf(nome):
    """
    Consulta quantidade de processos em aberto no STF.
    """
    driver_stf = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=options.to_capabilities())
    driver_stf.implicitly_wait(1)
    stf_url = 'http://portal.stf.jus.br/processos/listarPartes.asp?termo='
    driver_stf.get(stf_url + nome)
    sleep(randint(2, 5))
    quantidade = driver_stf.find_element_by_xpath('//*[@id="quantidade"]').text
    result = str(quantidade)
    driver_stf.quit()
    return "Quantidade de Processos: " + result


def jusbrasil(nome):
    """
    Pesquisa por processos públicos contendo o nome pesquisado.
    """
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
    """
    Pesquisa pelos termos do google.
    """
    return web_search_service.google_search(nome)


def check(nome: str):
    return {
        'background': {
            'stf': stf(nome),
            'jusbrasil': jusbrasil(nome),
            'google': google(nome)
        },
        'nome': nome
    }
