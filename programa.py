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

digite1 = "Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"
digiteGuardar = "Digite o índice do dado a ser guardado (0 a 4):"
digiteRemover = "Digite o índice do dado a ser removido (0 a 4):"
digiteCombinacao = "Digite a combinação desejada:"

listaDados = rolar_dados(5)
Estoque = []

print(imprime_cartela(cartela))
print(listaDados)
print(Estoque)
print(digite1)

while -1 in cartela['regra_simples'] and cartela['regra_avancada']:
    acao = int(input())
    if acao not in [0, 1, 2, 3, 4]:
        print("Opção inválida. Tente novamente.")
    elif acao == 1:
        print(digiteGuardar)
        dadoGuardar = int(input())
        lista = guardar_dado(listaDados, Estoque, dadoGuardar)
        listaDados = lista[0]
        Estoque = lista[1]
        print(listaDados)
        print(Estoque)
        print(digite1)








