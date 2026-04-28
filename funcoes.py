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

def calcula_pontos_sequencia_alta(listaDados):
    if 1 in listaDados and 2 in listaDados and 3 in listaDados and 4 in listaDados and 5 in listaDados:
        return 30
    elif 2 in listaDados and 3 in listaDados and 4 in listaDados and 5 in listaDados and 6 in listaDados:
        return 30

    return 0

def calcula_pontos_full_house(listaDados):
    lista1 = []
    lista2 = []
    # cria duas listas de validação para juntar o par e a trinca
    soma = 0
    for i in listaDados:
        if lista1 == []:
            lista1.append(i)
        elif lista2 == [] and i != lista1[0]:
            lista2.append(i)
        # adiciona um numero dos dados na lista de validação caso a mesma esteja vazia

        elif i == lista1[0]:
            lista1.append(i)
        elif i == lista2[0]:
            lista2.append(i)
        # adiciona um numero dos dados se este for igual ao dos que já estao na lista
        soma += i

    if len(lista1) == 3 and len(lista2) == 2:
        return soma
    elif len(lista2) == 3 and len(lista1) == 2:
        return soma
    else:
        return 0
    # confere se as listas possuem uma trinca e uma dupla e retorna o resultado

def calcula_pontos_quadra(listaDados):
    quantidade = {}
    for i in [1, 2, 3, 4, 5, 6]:
        quantidade[i] = 0
    # cria o dicionário com todos os valores das chaves em 0

    soma = 0
    for i in listaDados:
        quantidade[i] += 1
        soma += i
    # adiciona a quantidade de repetiçoes que cada dado teve e faz a soma

    for i, n in quantidade.items():
        if n >= 4:
            return soma
    return 0
    # confere se ha alguma repeticao maior ou igual a 4 e retorna o resultado

def calcula_pontos_quina(listaDados):
    quantidade = {}
    for i in [1, 2, 3, 4, 5, 6]:
        quantidade[i] = 0
    # cria o dicionário com todos os valores das chaves em 0

    for i in listaDados:
        quantidade[i] += 1
    # adiciona a quantidade de repetiçoes que cada dado teve e faz a soma

    for i, n in quantidade.items():
        if n >= 5:
            return 50
    return 0
    # confere se ha alguma repeticao maior ou igual a 4 e retorna o resultado

def calcula_pontos_regra_avancada(listaDados):
    pontuacoes = {}

    pontuacoes['cinco_iguais'] = calcula_pontos_quina(listaDados)
    pontuacoes['full_house'] = calcula_pontos_full_house(listaDados)
    pontuacoes['quadra'] = calcula_pontos_quadra(listaDados)
    pontuacoes['sem_combinacao'] = calcula_pontos_soma(listaDados)
    pontuacoes['sequencia_alta'] = calcula_pontos_sequencia_alta(listaDados)
    pontuacoes['sequencia_baixa'] = calcula_pontos_sequencia_baixa(listaDados)
    # roda as 5 funcoes e retorna um dicionario com os pontos obtidos em cada uma.

    return pontuacoes

def faz_jogada(listaDados, categoria, cartela):
    if categoria in ['1','2','3','4','5','6']:
        cartela['regra_simples'][int(categoria)] = calcula_pontos_regra_simples(listaDados)[int(categoria)]
    # se a categoria for simples, altera o valor do dicionário regra simples do dicionario cartela

    elif categoria in ['sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais']:
        cartela['regra_avancada'][categoria] = calcula_pontos_regra_avancada(listaDados)[categoria]
    # se a categoria for avançada, altera o valor do dicionário regra avançada do dicionario cartela
    return cartela

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)










    
