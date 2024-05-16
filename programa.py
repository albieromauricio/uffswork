# Atividade 8 da lista de funções
def correcao(gabarito, respostas):
    acertos = 0
    for i in range(len(gabarito)):
        if gabarito[i] == respostas[i]:
            acertos += 1
    return acertos
print('Separe as alternativas com espaço em branco(A B C D E).')
print(correcao(gabarito = list(map(str, input("Digite o gabarito: ").split())), respostas = list(map(str, input("Digite as respostas: ").split()))))