'''Escreva um programa para armazenar uma agenda de telefones usando
um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o
nome completo da pessoa. Seu programa deve ter as seguintes funções:
incluir_novo_nome – essa função acrescenta um novo nome na agenda, com
um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
incluir_telefone – essa função acrescenta um telefone em um nome existente na
agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja
incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo
nome.
excluir_telefone – essa função exclui um telefone de uma pessoa que
já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da
agenda.
excluir_nome – essa função exclui uma pessoa da agenda.
consultar_telefone – essa função retorna os telefones de uma pessoa
na agenda.'''

agenda = {}

def incluir_novo_nome(nome, *telefones):
    agenda[nome] = []
    for i in telefones:
        agenda[nome].append(i)

def incluir_telefone(nome, *telefones):
    if nome in agenda:
        for i in telefones:
            agenda[nome].append(i)
    else:
        print('Nome não encontrado')
        resposta = input('Deseja incluí-lo? (s/n) ')
        if resposta == 's':
            incluir_novo_nome(nome, *telefones)

def excluir_telefone(nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
        else:
            print('Telefone não encontrado')
    else:
        print('Nome não encontrado')

def excluir_nome(nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print('Nome não encontrado')

def consultar_telefone(nome):
    if nome in agenda:
        print(agenda[nome])
    else:
        print('Nome não encontrado')

