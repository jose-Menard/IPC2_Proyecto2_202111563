from clientes import Clientes

class Escritorios:
    def __init__(self, codigo = None, identificacion = None, nombreE = None,estado=None) -> None:
       self.codigo = codigo
       self.identificacion = identificacion
       self.nombreE = nombreE
       self.estado=estado
       self.clientes=Clientes()
       
       self.siguiente = None