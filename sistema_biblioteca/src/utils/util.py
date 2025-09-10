def gerar_id(lista):
    if not lista:
        return 1
    indice_ultimo = len(lista) - 1
    return  lista[indice_ultimo].get_id() + 1
