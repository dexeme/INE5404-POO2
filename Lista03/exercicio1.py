'''Escreva uma função que conta a frequência de ocorrência de cada
palavra em um texto (arquivo txt) e armazena tal quantidade em um dicionário, onde a
chave é a vogal considerada.'''

from Lista03 import exercicio1.txt

def main():
    texto = open('exercicio1.txt', 'r')
    texto = texto.read()
    texto = texto.split()
    vogais = ['a', 'e', 'i', 'o', 'u']
    dicionario = {}
    for i in range(len(vogais)):
        dicionario[vogais[i]] = 0
    for i in range(len(texto)):
        for j in range(len(vogais)):
            if texto[i][0] == vogais[j]:
                dicionario[vogais[j]] += 1
    print(dicionario)

