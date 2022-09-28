'''Não existem instâncias de Animal, Mamifero e Ave, somente dos seus sub-tipos
Todos os animais possuem um tamanho de passo e quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU " tamanhoPasso
As aves quando se movem, retornam a mensagem: "ANIMAL: DESLOCOU "+tamanhoPasso+" VOANDO"
Todos os animais produzem algum tipo de som com um volume, mas cada um do seu jeito:
Gato (miar): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: MIAU"
Cachorro (latir): "MAMIFERO: PRODUZ SOM: "+volumeSom+ " SOM: AU"
Canarinho (cantar): "AVE: PRODUZ SOM: PIU"
Somente as aves voam (que é a mesma coisa que mover para uma ave)
Somente os canarinhos cantam 
Cachorros tem tamanhoPasso = 3 e volumeSom = 3
Gatos tem tamanhoPasso = 2 e volumeSom = 2
Aves tem tamanhoPasso e alturaVoo parametrizáveis no construtor'''

from abc import ABC, abstractmethod


class Animal(ABC):
	def __init__(self, tamanho_passo: int):
		self.__tamanho_passo = tamanho_passo

	@property
	def tamanho_passo(self):
		return self.__tamanho_passo

	@tamanho_passo.setter
	def tamanho_passo(self, tamanho_passo):
		self.__tamanho_passo = tamanho_passo

	def mover(self):
		return f'ANIMAL: DESLOCOU {self.tamanho_passo}'

	@abstractmethod
	def produzirSom(self):
		pass