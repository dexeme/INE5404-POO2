#Warmup 1
from math import math

class Televisao:
    def __init__(self, ligada, canal, tamanho, marca, canal_min=2, canal_max=14):
        self.ligada = ligada
        self.canal = canal
        self.tamanho = tamanho
        self.marca = marca
        self.canal_minimo = 1
        self.canal_maximo = 99

tv_1 = Televisao(True, 4, 32, "Samsung")
tv_2 = Televisao(True, 4, 23, "Aoc")

print(tv_1.ligada, tv_1.canal, tv_1.tamanho, tv_1.marca)
print(tv_2.ligada, tv_2.canal, tv_2.tamanho, tv_2.marca)

def muda_canal_para_cima(self, tv, canal):
    if tv.canal > tv.canal_maximo:
        tv.canal = tv.canal_minimo
    else:
        tv.canal += 1
    return tv.canal

def muda_canal_para_baixo(self, tv, canal):
    if tv.canal < tv.canal_minimo:
        tv.canal = tv.canal_maximo
    else:
        tv.canal -= 1
    return tv.canal

tv_3 = Televisao(canal_max="Globo",canal_min="Sbt")
tv_4 = Televisao(canal_max="Record",canal_min="Band")

class Estado:
    def __init__(self, nome, sigla, cidades=[]):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades
        self.populacao = 0
        for cidade in self.cidades:
            self.populacao += cidade.populacao


class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
       
sao_paulo = Estado("Sao Paulo", 10000000, "SP")
santa_catarina = Estado("Santa Catarina", 500000, "SC")
acre = Estado("Acre", 100000, "AC")
rio_de_janeiro = Cidade("Rio de Janeiro", 5000000)
florianopolis = Cidade("Florianopolis", 500000)
palhoca = Cidade("Palhoca", 100000)
blumenau = Cidade("Blumenau", 200000)
curitiba = Cidade("Curitiba", 300000)
pernambuco = Cidade("Pernambuco", 100000)
cuiaba = Cidade("Cuiaba", 100000)

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcula_distancia(self, outra_coordenada):
        x_diff = (self.x - outra_coordenada.x) ** 2
        y_diff = (self.y - outra_coordenada.y) ** 2
        return (x_diff + y_diff) ** 0.5

    def compara_coordenada(self, outra_coordenada):
        if self.x == outra_coordenada.x and self.y == outra_coordenada.y:
            return True
        else:
            return False
    
    def coordenada_polar(self):
        raio = (self.x ** 2 + self.y ** 2) ** 0.5
        angulo = math.atan2(self.y, self.x)
        return (raio, angulo)

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

class Retangulo:
    def __init__(self, lado_menor, lado_maior):
        self.lado_menor = lado_menor
        self.lado_maior = lado_maior

class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def soma(self, outra_fracao):
        numerador = self.numerador * outra_fracao.denominador + self.denominador * outra_fracao.numerador
        denominador = self.denominador * outra_fracao.denominador
        return Fracao(numerador, denominador)

    def subtracao(self, outra_fracao):
        numerador = self.numerador * outra_fracao.denominador - self.denominador * outra_fracao.numerador
        denominador = self.denominador * outra_fracao.denominador
        return Fracao(numerador, denominador)

    def multiplicacao(self, outra_fracao):
        numerador = self.numerador * outra_fracao.numerador
        denominador = self.denominador * outra_fracao.denominador
        return Fracao(numerador, denominador)

    def divisao(self, outra_fracao):
        numerador = self.numerador * outra_fracao.denominador
        denominador = self.denominador * outra_fracao.numerador
        return Fracao(numerador, denominador)

    def imprime_formato_numerador(self):
        return f"{self.numerador}/{self.denominador}"

    def inverter_fracao(self):
        return f"{self.denominador}/{self.numerador}"

    def retorna_em_valor_real(self):
        return self.numerador / self.denominador

    def criar_fracao_a_partir_de_numero_real(self, numero_real):
        self.numerador = numero_real
        self.denominador = 1
        return Fracao(self.numerador, self.denominador)