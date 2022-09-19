'''Uma pista de Kart permite 10 voltas para cada um de 6 corredores.
Escreva um programa que leia todos os tempos em segundos e os guarde em um
dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta
da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O
campeão é o que tem a menor média de tempos'''


def melhor_volta():
    tempos = {}
    for i in range(6):
        nome = input('Nome do corredor: ')
        tempos[nome] = []
        for j in range(10):
            tempo = float(input('Tempo da volta: '))
            tempos[nome].append(tempo)
    melhor_volta = 1000000
    for i in tempos:
        for j in tempos[i]:
            if j < melhor_volta:
                melhor_volta = j
                nome_melhor_volta = i
    print('Melhor volta: ', melhor_volta, 'segundos')
    print('Nome do corredor: ', nome_melhor_volta)
    return tempos


def classificacao(tempos):
    for i in range(6):
        media = 0
        for j in tempos:
            media += tempos[j][i]
        media /= 6
        print('Média da volta ', i + 1, ': ', media, 'segundos')


tempos = melhor_volta()
classificacao(tempos)