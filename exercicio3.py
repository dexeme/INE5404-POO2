class Polinomio():
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def entrada():
        coeficientes = []
        while True:
            try:
                coeficientes.append(int(input('Digite o coeficiente: ')))
            except ValueError:
                break
        return coeficientes