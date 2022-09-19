'''Escreva um programa que lê duas notas de vários alunos e armazena tais
notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve
terminar quando for lida uma string vazia como nome. Escreva uma função que retorna
a média do aluno, dado seu nome.'''

notas = {}

while True:
    nome = input('Nome: ')
    if nome == '':
        break
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notas[nome] = [nota1, nota2]

def media(nome):
    return (notas[nome][0] + notas[nome][1]) / 2

nome = input('Nome do aluno: ')
print('Média: ', media(nome))



