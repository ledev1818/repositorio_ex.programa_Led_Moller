import random

def rolar_dados(n):
    listaDados = []
    for i in range(n):
        listaDados.append(random.randint(1, 6))
    return listaDados

def guardar_dado(dadosRolados, dadosEstoque, dadoGuardar):
    novosRolados = []
    novoEstoque = []
    for i in dadosEstoque:
        novoEstoque.append(i)
    novoEstoque.append(dadosRolados[dadoGuardar])
    # cria a nova lista de estoque, adicionando os antigos e o novo dado

    for i in range(len(dadosRolados)):
        if i != dadoGuardar:
            novosRolados.append(dadosRolados[i])
    # cria a nova lista de dados rolados, pulando o dado a ser guardado

    return [novosRolados, novoEstoque]

def remover_dado(dadosRolados, dadosEstoque, dadoRemover):
    novosRolados = []
    novoEstoque = []
    for i in dadosRolados:
        novosRolados.append(i)
    novosRolados.append(dadosEstoque[dadoRemover])
    # cria a nova lista de dados rolados e adiciona o dado que será removido do estoque

    for i in range(len(dadosEstoque)):
        if i != dadoRemover:
            novoEstoque.append(dadosEstoque[i])
    # cria um novo estoque sem o dado removido

    return [novosRolados, novoEstoque]

def calcula_pontos_regra_simples(listaDados):
    pontuacao = {}
    for i in [1, 2, 3, 4, 5, 6]:
        pontuacao[i] = 0
    # cria o dicionário com todos os valores das chaves em 0

    for i in listaDados:
        pontuacao[i] += i
    # adiciona os valores dos dados no diconário
    return pontuacao

def calcula_pontos_soma(listaDados):
    soma = 0
    for i in listaDados:
        soma += i
    return soma

def calcula_pontos_sequencia_baixa(listaDados):
    if 1 in listaDados and 2 in listaDados and 3 in listaDados and 4 in listaDados:
        return 15
    elif 2 in listaDados and 3 in listaDados and 4 in listaDados and 5 in listaDados:
        return 15
    elif 3 in listaDados and 4 in listaDados and 5 in listaDados and 6 in listaDados:
        return 15
    
    return 0









    
