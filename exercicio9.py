
class CampoMinado:
    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.tabuleiro = []
        self.campo = []
        self.criar_tabuleiro()
        self.criar_campo()
        self.posicionar_bombas()
        self.contar_bombas()

    def criar_tabuleiro(self):
        for i in range(self.linhas):
            self.tabuleiro.append([])
            for j in range(self.colunas):
                self.tabuleiro[i].append(' ')

    def criar_campo(self):
        for i in range(self.linhas):
            self.campo.append([])
            for j in range(self.colunas):
                self.campo[i].append(0)

    def posicionar_bombas(self):
        import random
        for i in range(self.bombas):
            linha = random.randint(0, self.linhas - 1)
            coluna = random.randint(0, self.colunas - 1)
            self.campo[linha][coluna] = '*'

    def contar_bombas(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.campo[i][j] != '*':
                    self.campo[i][j] = self.contar_vizinhos(i, j)

    def contar_vizinhos(self, linha, coluna):
        contador = 0
        for i in range(linha - 1, linha + 2):
            for j in range(coluna - 1, coluna + 2):
                if i >= 0 and i < self.linhas and j >= 0 and j < self.colunas:
                    if self.campo[i][j] == '*':
                        contador += 1
        return contador

    def mostrar_tabuleiro(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                print(self.tabuleiro[i][j], end=' ')
            print()

    def mostrar_campo(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                print(self.campo[i][j], end=' ')
            print()

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            linha = int(input('Digite a linha: '))
            coluna = int(input('Digite a coluna: '))
            if self.campo[linha][coluna] == '*':
                print('Você perdeu!')
                break
            else:
                self.tabuleiro[linha][coluna] = self.campo[linha][coluna]
                if self.tabuleiro == self.campo:
                    print('Você ganhou!')
                    break

CampoMinado.jogar(CampoMinado(10, 10, 10))
