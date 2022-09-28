from animal import Animal
from abc import ABC, abstractmethod


class Ave(Animal):
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo):
        self.__altura_voo = altura_voo

    def mover(self):
        return f'ANIMAL: DESLOCOU {self.tamanho_passo} VOANDO'

    @abstractmethod
    def produzirSom(self):
        pass