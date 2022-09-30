class Configuracion:
    def __init__(self, idC = None, idE = None, idP = None) -> None:

        self.idC=idC
        self.idE=idE
        self.idP=idP

        self.siguiente = None
        self.anterior = None