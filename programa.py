import random
from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import calcula_pontos_regra_simples
from funcoes import calcula_pontos_soma
from funcoes import calcula_pontos_sequencia_baixa
from funcoes import calcula_pontos_sequencia_alta
from funcoes import calcula_pontos_full_house
from funcoes import calcula_pontos_quadra
from funcoes import calcula_pontos_quina
from funcoes import calcula_pontos_regra_avancada
from funcoes import faz_jogada
from funcoes import imprime_cartela

cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

combinacoes = []
for i, n in cartela.items():
    for j, k in n.items():
        combinacoes.append(j)
# cria uma lista com todas as combinacoes do jogo

digite1 = "Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"
digiteGuardar = "Digite o índice do dado a ser guardado (0 a 4):"
digiteRemover = "Digite o índice do dado a ser removido (0 a 4):"
digiteCombinacao = "Digite a combinação desejada:"

listaDados = rolar_dados(5)
Estoque = []
reroladas = 0
rodada = 0

imprime_cartela(cartela)

while rodada < 12:
    print(f'Dados rolados: {listaDados}')
    print(f'Dados guardados: {Estoque}')
    print(digite1)
    acao = input('')
    if acao not in ['0', '1', '2', '3', '4']: 
        print("Opção inválida. Tente novamente.")

    elif acao == '1': # segue codigo para a guardar o dado
        print(digiteGuardar)
        dadoGuardar = int(input(''))
        lista = guardar_dado(listaDados, Estoque, dadoGuardar)
        listaDados = lista[0]
        Estoque = lista[1]

    elif acao == '2': # segue o codigo para remover um dado do estoque
        print(digiteRemover)
        dadoRemover = int(input(''))
        lista = remover_dado(listaDados, Estoque, dadoRemover)
        listaDados = lista[0]
        Estoque = lista[1]

    elif acao == '3': # segue o codigo para rerolagem (após a ação 0, as reroladas devem ser zeradas)
        if reroladas == 2:
            print("Você já usou todas as rerrolagens.")
        else:
            listaDados = rolar_dados(len(listaDados))
            reroladas += 1

    elif acao == '4': 
        imprime_cartela(cartela)

    elif acao == '0':
        terminada = False # variavel para determinar se a pontuacao foi computada (combinacao valida nao utilizada)
        listaDados += Estoque # junta todos os dados para pontuar

        while terminada == False:
            print(digiteCombinacao)
            combinacao = input('')
            if combinacao in ['1','2','3','4','5','6']:
                combinacao = int(combinacao)

            if combinacao not in combinacoes:
                print("Combinação inválida. Tente novamente.")
            else:
                if combinacao in combinacoes[0:6]:
                    if cartela['regra_simples'][combinacao] == -1:
                        combinacao = str(combinacao)
                        cartela = faz_jogada(listaDados, combinacao, cartela)
                        terminada = True
                        rodada += 1
                    else:
                        print("Essa combinação já foi utilizada.")

                elif combinacao in combinacoes[6:]:
                    if cartela['regra_avancada'][combinacao] == -1:
                        combinacao = str(combinacao)
                        cartela = faz_jogada(listaDados, combinacao, cartela)
                        terminada = True
                        rodada += 1
                    else:
                        print("Essa combinação já foi utilizada.")

        listaDados = rolar_dados(5)
        Estoque = []
        reroladas = 0

imprime_cartela(cartela)

pontosSimples = 0
pontosAvancado = 0
bonus = 0
for i, n in cartela.items():
    for j, k in n.items():
        if i == 'regra_simples':
            pontosSimples += k
        elif i == 'regra_avancada':
            pontosAvancado += k

if pontosSimples >= 63:
    bonus = 35

pontuacaoTotal = pontosAvancado + pontosSimples + bonus
print(f"Pontuação total: {pontuacaoTotal}")













