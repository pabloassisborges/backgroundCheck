from bgcheck.services import tribunais_service, search_service


def gerar_relatorio(nome):
    """
    Gera um relatório completo sobre o nome pesquisado.
    """
    return {
        'nome': nome,
        'tribunais': {
            'jusbrasil': tribunais_service.consulta_jusbrasil(nome),
            'stf': tribunais_service.consulta_stf(nome)
        },
        'google': search_service.buscar_nome(nome)
    }
