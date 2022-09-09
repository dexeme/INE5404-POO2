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

    def grau_do_polinomio(self):
        return len(self.coeficientes) - 1
    
    def somar_polinomios(self, polinomio):
        if len(self.coeficientes) > len(polinomio.coeficientes):
            maior = self.coeficientes
            menor = polinomio.coeficientes
        else:
            maior = polinomio.coeficientes
            menor = self.coeficientes
        
        for i in range(len(menor)):
            maior[i] += menor[i]
        
        return maior
    
    def multiplicar_polinomios(self, polinomio):
        resultado = [0] * (len(self.coeficientes) + len(polinomio.coeficientes) - 1)
        for i in range(len(self.coeficientes)):
            for j in range(len(polinomio.coeficientes)):
                resultado[i + j] += self.coeficientes[i] * polinomio.coeficientes[j]
        return resultado