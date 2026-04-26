import random

def rolar_dados(n):
    listaDados = []
    for i in range(n):
        listaDados.append(random.randint(1, 6))
    return listaDados
