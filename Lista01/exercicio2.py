
class Biblioteca():
    def __init__(self, livros):
        self.livros = livros

class Livro():
    def __init__(self, titulo, autor, ano, editora, edicao, volume):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume
    
    def cadastrar_livro(self):
        self.titulo = input('Digite o título do livro: ')
        self.autor = input('Digite o autor do livro: ')
        self.ano = input('Digite o ano do livro: ')
        self.editora = input('Digite a editora do livro: ')
        self.edicao = input('Digite a edição do livro: ')
        self.volume = input('Digite o volume do livro: ')
        return self

    def buscar_livro(self, titulo):
        if self.titulo == titulo:
            return self
        else:
            return False

