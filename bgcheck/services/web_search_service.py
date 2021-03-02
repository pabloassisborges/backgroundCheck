"""
Realiza uma busca mais geral em websites como google, facebook, etc. Retorna
resultados relacionados ao nome pesquisado, a presença desse nome em redes
sociais, etc.
"""
from googlesearch import search


def google_search(nome: str, num_results=20):
    return search(nome, num_results=num_results, lang='pt-br')
