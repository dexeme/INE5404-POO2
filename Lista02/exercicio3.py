'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

contador = 1
soma = 0
lista_de_notas = []

for i in range (4):

    nota = int(input(f'Insira a {contador}ª nota: '))
    contador += 1
    lista_de_notas.append(nota)
    soma += nota

print(f'Notas: {lista_de_notas}')
print(f'Média: {soma/4}')