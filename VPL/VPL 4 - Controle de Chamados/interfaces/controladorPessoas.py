from interfaces import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):

    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        jaesta = False
        for cliente in self.clientes:
            if codigo == cliente.codigo:
                jaesta = True
                break
        if not jaesta:
            cliente = Cliente(nome, codigo)
            self.__clientes.append(cliente)
            return cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        jaesta = False
        for tecnico in self.tecnicos:
            if codigo == tecnico.codigo:
                jaesta = True
                break
        if not jaesta:
            tecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(tecnico)
            return tecnico