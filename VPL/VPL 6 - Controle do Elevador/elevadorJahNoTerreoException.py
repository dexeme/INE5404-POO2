class ElevadorJahNoTerreoException(Exception):
    def __init__(self):
        self.message = "Elevador já está no térreo"
        super().__init__(self.message)