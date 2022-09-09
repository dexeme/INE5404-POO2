
class BaralhoDeCartas:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def embaralhar(self):
        import random
        random.shuffle(self.cartas)

    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)

    def mostrar_cartas_embaralhadas(self):
        self.embaralhar()
        self.mostrar_cartas()