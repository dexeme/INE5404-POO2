'''Exercício 17.​ Em uma competição de salto em distância cada atleta tem direito a cinco
saltos. O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
programa deve ser encerrado quando não for informado o nome do atleta. A saída do
programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m'''



nome = str(input('Digite o nome do atleta >>> ')).title()
contador = 1
lista_de_distancias = []
entrada_valida = True
while entrada_valida:
    if nome != '':
        distancia = int(input(f'Digite a {contador}º distância >>> '))
        while distancia < 0:
            distancia = int(input(f'Você não pode inserir um valor negativo!\nDigite a {contador}º distância >>> '))
        lista_de_distancias.append(distancia)
        contador += 1
    if contador > 5:
        entrada_valida = False


total_de_saltos = 0
for salto in lista_de_distancias:
    total_de_saltos += salto

media_de_saltos = (total_de_saltos/5)

print(f'Atleta: {nome}')
print(f'Primeiro Salto: {lista_de_distancias[0]}m')
print(f'Segundo Salto: {lista_de_distancias[1]}m')
print(f'Terceiro Salto: {lista_de_distancias[2]}m')
print(f'Quarto Salto: {lista_de_distancias[3]}m')
print(f'Quinto Salto: {lista_de_distancias[4]}m')
print('Resultado final:')
print(f'Atleta: {nome}')
print(f'Saltos: {lista_de_distancias[0]} - {lista_de_distancias[1]} - {lista_de_distancias[2]} - {lista_de_distancias[3]} - {lista_de_distancias[4]}')
print(f'Média dos saltos: {media_de_saltos}m')