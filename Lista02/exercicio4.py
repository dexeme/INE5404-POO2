'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas
consoantes foram lidas. Imprima as consoantes.'''

vetor = [x for x in input().strip().split()]

vogais = 0
for numero in vetor:
    if numero in 'aeiou':
        vogais += 1

print(f'{10-vogais}')