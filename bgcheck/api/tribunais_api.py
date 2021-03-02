from bgcheck.services import tribunais_service


def consulta_tribunais(nome: str):
    return {
        'nome': nome,
        'jusbrasil': tribunais_service.consulta_jusbrasil(nome),
        'stf': tribunais_service.consulta_stf(nome)
    }
