def calcular_lpa(lucro_liquido, numero_acoes):
    if numero_acoes <= 0:
        raise ValueError("Número de ações inválido")
    return lucro_liquido / numero_acoes
