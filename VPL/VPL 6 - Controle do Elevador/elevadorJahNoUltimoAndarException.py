class ElevadorJahNoUltimoAndarException(Exception):
    def __init__(self):
        self.message = "Elevador já no último andar"
        super().__init__(self.message)