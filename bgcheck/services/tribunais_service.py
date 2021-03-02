from time import sleep

from bgcheck.factory.chrome import chrome


def consulta_jusbrasil(nome: str) -> list:

    def element_to_info(element):
        """Converte um resultado da busca em um objeto JSON (Dicionario)."""
        bio = element.find_elements_by_css_selector('div.EntitySnippet-bio div')

        return {
            'nome': element.find_element_by_css_selector('a.EntitySnippet-anchor').text,
            'link': element.find_element_by_css_selector('a.EntitySnippet-anchor').get_attribute('href'),
            'processos': bio[0].text,
            'tribunais relevantes': bio[1].text,
            'parte mais citada': bio[2].text
        }

    browser = chrome()
    browser.implicitly_wait(1)
    browser.get(f'https://www.jusbrasil.com.br/consulta-processual/busca?q={nome}')

    sleep(1)

    # Extrai os resultados encontrados na página de busca do Jusbrasil sem os
    # indices.
    result = browser.find_element_by_xpath('//*[@id="app-root"]/div/div/div[1]/div[2]/div[2]') \
        .find_elements_by_css_selector('div.EntitySnippet-item.EntitySnippet--expanded.EntitySnippet-topic')

    response = list(map(element_to_info, result))

    browser.quit()

    return response


def consulta_stf(nome: str) -> list:

    def element_to_info(element):
        """Converte um resultado da busca em um objeto JSON (Dicionario)."""
        info = element.find_elements_by_tag_name('td')

        return {
            'identificação': info[0].text,
            'link': info[0].find_element_by_tag_name('a').get_attribute('href'),
            'parte': info[1].text,
            'numero': info[2].text,
            'data atuação': info[3].text,
            'meio': info[4].text,
            'publicidade': info[5].text,
            'tramite': info[6].text
        }

    browser = chrome()
    browser.implicitly_wait(1)
    browser.get(f'http://portal.stf.jus.br/processos/listarPartes.asp?termo={nome}')

    sleep(1)

    quantidade = browser.find_element_by_xpath('//*[@id="quantidade"]').text

    # Listando os processos encontrados no site do STF
    result = browser.find_element_by_css_selector('table#tabela_processos') \
        .find_element_by_tag_name('tbody') \
        .find_elements_by_tag_name('tr')[1:]

    # Extraindo informações do processo dos resultados encontrados no site do STF
    processos = list(map(element_to_info, result))

    browser.quit()

    return {
        'quantidade': f'{quantidade} Processo(s) encontrado(s)',
        'processos': processos
    }
