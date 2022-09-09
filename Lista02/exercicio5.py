'''Faça um Programa que leia 20 números inteiros e armazene-os num
vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor
impar. Imprima os três vetores.'''


vetor = [int(x) for x in input().split()]

par = []
impar = []

for num in vetor:
    if (num%2) == 0:
        par.append(num)
    else:
        impar.append(num)

print(vetor)
print(par)
print(impar)