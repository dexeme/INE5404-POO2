'''Escreva uma função que apaga do dicionário anterior, todas as palavras
que sejam ‘stopwords’. Ver https://gist.github.com/alopes/5358189'''

from Lista03 import exercicio1

def apagar_do_dicionario():
    exercicio1.frequencia()
    dicionario = exercicio1.dicionario
    stopwords = stopwords.txt # Arquivo com as stopwords
    stopwords = stopwords.read()
    stopwords = stopwords.split()
    for i in range(len(stopwords)):
        if stopwords[i] in dicionario:
            del dicionario[stopwords[i]]
    print(dicionario)




