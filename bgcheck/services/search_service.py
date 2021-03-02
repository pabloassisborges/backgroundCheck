from googlesearch import search


def buscar_nome(nome: str, num_results=20):
    return search(nome, num_results, lang='pt-br')
