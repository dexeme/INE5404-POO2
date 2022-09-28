from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andarAtual, totalAndaresPredio,
                 capacidade, totalPessoas):
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas

    @property
    def andarAtual(self):
        return self.__andarAtual

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def totalPessoas(self):
        return self.__totalPessoas

    @property
    def totalAndaresPredio(self):
        return self.__totalAndaresPredio

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio):
        self.__totalAndaresPredio = totalAndaresPredio

    def descer(self) -> str:
        if self.__andarAtual == 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andarAtual -= 1
            return 'Elevador desceu um andar.'

    def entraPessoa(self) -> str:
        if self.__totalPessoas == self.capacidade:
            raise ElevadorCheioException
        else:
            self.__totalPessoas += 1
            return 'Uma pessoa entrou.'

    def saiPessoa(self) -> str:
        if self.__totalPessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.__totalPessoas -= 1
            return 'Uma pessoa saiu.'

    def subir(self) -> str:
        if self.__andarAtual == self.__totalAndaresPredio - 1:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andarAtual += 1
            return 'Elevador subiu um andar.'
