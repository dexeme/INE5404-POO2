class ElevadorJahVazioException(Exception):
    def __init__(self):
        super().__init__()
        self.__mensagem = "O elevador já está vazio!"

    def __str__(self):
        return self.__mensagem