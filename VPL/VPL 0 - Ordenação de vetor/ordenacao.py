"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
   Aluna: Diana Faustino de  Siqueira - Matrícula 22102193
"""

class Ordenacao():

    def __init__(self, array_para_ordenar: list):
        self.array_para_ordenar = array_para_ordenar
        
    def ordena(self):
        for i in range(len(self.array_para_ordenar)):
            for j in range(i+1, len(self.array_para_ordenar)):
                if self.array_para_ordenar[i] > self.array_para_ordenar[j]:
                    self.array_para_ordenar[i], self.array_para_ordenar[j] = self.array_para_ordenar[j], self.array_para_ordenar[i]
        return self.array_para_ordenar

    def toString(self):
        self.ordena()
        b = [str(i) for i in self.array_para_ordenar]
        return str(','.join(b))