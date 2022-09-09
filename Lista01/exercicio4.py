class SeriesMatematicas():
    def __init__(self, n):
        self.n = n

    def Fibonacci(self):
        a, b = 0, 1
        for i in range(self.n):
            a, b = b, a + b
        return a
    
    def Fatorial(self):
        resultado = 1
        for i in range(1, self.n + 1):
            resultado *= i
        return resultado
    
    def Fibonarial(self):
        return self.Fibonacci() * self.Fatorial()
    
    def Primo(self):
        if self.n == 1:
            return False
        for i in range(2, self.n):
            if self.n % i == 0:
                return False
        return True