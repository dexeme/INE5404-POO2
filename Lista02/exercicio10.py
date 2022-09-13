'''Exercício 10. ​Faça um Programa que leia dois vetores com 10 elementos cada. Gere
um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.'''


for i in range(1):
    vetor1 = [int(x) for x in input().strip().split()]
    vetor2 = [int(x) for x in input().strip().split()]
    while len(vetor1) != 10 or len(vetor2) != 10:
        vetor1 = [int(x) for x in input('O vetor deve ter 10 elementos! >>> ').strip().split()]
        vetor2 = [int(x) for x in input('O vetor deve ter 10 elementos! >>> ').strip().split()]

vetor_junto = []
for i in vetor1:
    vetor_junto.append(i)
for j in vetor2:
    vetor_junto.append(j)

vetor_final = []
cont_1 = 0
cont_2 = 1
for i in range(11):
    vetor_final.append(vetor_junto[cont_1])
    cont_1 += 2
    vetor_final.append(vetor_junto[(20-cont_2)])
    cont_2 += 2
    if cont_2 >= 19:
        break
print(vetor_final)





