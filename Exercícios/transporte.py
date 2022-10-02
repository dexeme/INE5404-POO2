'''Crie uma classe chamada Transporte para representar um veículo de transporte. A classe possui cinco atributos, denominados:
nome: nome do veículo de transporte;
altura: altura do veículo de transporte em metros (m);
comprimento: comprimento do veículo de transporte em metros (m);
carga: capacidade de carga do veículo de transporte em toneladas (t);
velocidade: velocidade do veículo de transporte em quilômetros por hora (km/h)
Estenda a classe Transporte para implementar uma classe chamada TransporteAereo para representar um veículo de transporte aéreo. A classe possui dois atributos, denominados:

autonomia: autonomia de voo do veículo de transporte aéreo em quilômetros (km);
envergadura: envergadura da asa do veículo de transporte aéreo em metros (m).

Estenda a classe Transporte para implementar uma classe chamada TransporteTerrestre para representar um veículo de transporte terrestre. A classe possui dois atributos, denominados:
motor: motor do veículo de transporte terrestre, do tipo String;
rodas: rodas do veículo de transporte terrestre, do tipo String.

Estenda a classe Transporte para implementar uma classe chamada TransporteAquatico para representar um veículo de transporte marítimo. A classe possui dois atributos, denominados:
boca: boca náutica do veículo de transporte marítimo em metros (m);
calado: calado do veículo de transporte marítimo em metros (m).

Desenvolva uma classe chamada Catálogo para representar um catálogo de veículos de transporte, implementando os métodos para inserção e apresentação (mostrar) dos veículos de transporte cadastrados.
Envie o jupyter notebook com o seu exercício resolvido aqui.
 '''

class Transporte:
    def __init__(self, nome, altura, comprimento, carga, velocidade):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade
    

class TransporteAereo(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, autonomia, envergadura):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.autonomia = autonomia
        self.envergadura = envergadura

class TransporteTerrestre(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, motor, rodas):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.motor = motor
        self.rodas = rodas

class TransporteAquatico(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, boca, calado):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.boca = boca
        self.calado = calado

class Catalogo:
    def __init__(self):
        self.lista = []
    
    def inserir(self, veiculo):
        self.lista.append(veiculo)
    
    def mostrar(self):
        for i in range(len(self.lista)):
            print(self.lista[i].nome)
            print(self.lista[i].altura)
            print(self.lista[i].comprimento)
            print(self.lista[i].carga)
            print(self.lista[i].velocidade)
            if isinstance(self.lista[i], TransporteAereo):
                print(self.lista[i].autonomia)
                print(self.lista[i].envergadura)
            elif isinstance(self.lista[i], TransporteTerrestre):
                print(self.lista[i].motor)
                print(self.lista[i].rodas)
            elif isinstance(self.lista[i], TransporteAquatico):
                print(self.lista[i].boca)
                print(self.lista[i].calado)
            print('')

catalogo = Catalogo()
catalogo.inserir(TransporteAereo('Boeing 747', 70, 70, 100, 100, 100, 100))
catalogo.inserir(TransporteTerrestre('Fusca', 70, 70, 100, 100, 'V8', '4'))
catalogo.inserir(TransporteAquatico('Navio', 70, 70, 100, 100, 100, 100))
catalogo.mostrar()

