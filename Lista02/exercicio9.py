'''Exercício 9. ​Faça um Programa que leia um vetor A com 10 números inteiros, calcule
e mostre a soma dos quadrados dos elementos do vetor.'''


vetor = [int(x) for x in input().strip().split()]

while len(vetor) != 10:
    vetor = [int(x) for x in input('O vetor deve ter 10 elementos! >>> ').strip().split()]

soma = 0
for numero in vetor:
    soma += (numero**2)

print(soma)