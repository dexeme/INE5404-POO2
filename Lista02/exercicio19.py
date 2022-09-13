'''Uma empresa de pesquisas precisa tabular os resultados da seguinte
enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e
informe ao final o resultado da mesma. O programa deverá ler os valores até ser
informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores
além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das
opções devem ser armazenados numa lista. Após os dados terem sido completamente
informados, o programa deverá calcular a percentual de cada um dos concorrentes e
informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o
seguinte:
Sistema Operacional Votos %
------------------- ----- ---
Windows Server 1500 17%
Unix 3500 40%
Linux 3000 34%
Netware 500 5%
Mac OS 150 2%
Outro 150 2%
------------------- -----
Total 8800
O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos
votos.'''

lista_de_escolhas = []
while True:
    escolha = input()
    if escolha not in '0123456':
        escolhas = input('Erro, digite novamente!\n>>> ')
    else: 
        lista_de_escolhas.append(escolha)
    if escolha == '0':
        break


total_de_pessoas = (len(lista_de_escolhas)-1)

votos_1 = lista_de_escolhas.count('1')
votos_2 = lista_de_escolhas.count('2')
votos_3 = lista_de_escolhas.count('3')
votos_4 = lista_de_escolhas.count('4')
votos_5 = lista_de_escolhas.count('5')
votos_6 = lista_de_escolhas.count('6')

total_de_votos = []
total_de_votos.append(votos_1)
total_de_votos.append(votos_2)
total_de_votos.append(votos_3)
total_de_votos.append(votos_4)
total_de_votos.append(votos_5)
total_de_votos.append(votos_6)

maior = max(total_de_votos)
index_do_maior = total_de_votos.index(maior)
if index_do_maior == 0:
    mais_votado = 'Windows Server'
elif index_do_maior == 1:
    mais_votado = 'Unix'
elif index_do_maior == 2:
    mais_votado = 'Linux'
elif index_do_maior == 3:
    mais_votado = 'Netware'
elif index_do_maior == 4:
    mais_votado = 'Mac OS'
elif index_do_maior == 5:
    mais_votado = 'Outro'



print('Sistema Operacional Votos %') 
print('------------------- ----- ---')
print(f'Windows Server {votos_1} {(votos_1)/(total_de_pessoas) * 100:.2f}%')
print(f'Unix {votos_2} {(votos_2)/(total_de_pessoas) * 100:.2f}%')
print(f'Linux {votos_3} {(votos_3)/(total_de_pessoas) * 100:.2f}%')
print(f'Netware {votos_4} {(votos_4)/(total_de_pessoas) * 100:.2f}%')
print(f'Mac OS {votos_5} {(votos_5)/(total_de_pessoas) * 100:.2f}%')
print(f'Outro {votos_6} {(votos_6)/(total_de_pessoas) * 100:.2f}%')
print('------------------- -----')
print(f'Total {total_de_pessoas}')
print(f'O Sistema Operacional mais votado foi o {mais_votado}, com {maior} votos, correspondendo a {(maior/total_de_pessoas)*100:.2f}% dos')
print('votos.')