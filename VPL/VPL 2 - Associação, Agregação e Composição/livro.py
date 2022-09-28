from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = []
        self.autores.append(autor)
        numeroCapitulo = numeroCapitulo
        tituloCapitulo = tituloCapitulo
        self.__capitulos = []
        
    @property
    def codigo(self):
        return self.__codigo    
    @property
    def ano(self):
        return self.__ano
    @property
    def editora(self):
        return self.__editora
    @property
    def autores(self):
        return self.__autores
    @property
    def titulo(self):
        return self.__titulo
        
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
    
    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano
    
    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora
        
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    def incluirAutor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor not in self.__autores:
                self.__autores.append(autor)
    
    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        exist = False
        for capitulo in self.__capitulos:
            if capitulo.titulo == tituloCapitulo:
                exist = True
                break
        if exist is False:  
            self.__capitulos.append(Capitulo(numeroCapitulo, tituloCapitulo))
        else:
            print("Capítulo já existe")

    def excluirCapitulo(self, tituloCapitulo: str):
        capitulo = self.findCapituloByTitulo(tituloCapitulo)
        if capitulo is not None:
            self.__capitulos.remove(capitulo)
        else:
            print("Capítulo não existe")

    def excluirAutor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor in self.__autores:
                self.__autores.remove(autor)
            else:
                print("Autor não existe")
    

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == tituloCapitulo:
                return capitulo
        return None
