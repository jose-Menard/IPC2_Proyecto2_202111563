
from listaDobleTransa import ListaDobleTransa


class Clientes:
    def __init__(self, dpi = None, nombre = None ) -> None:
       self.dpi = dpi
       self.nombre = nombre
       self.transaNueva=ListaDobleTransa()

       self.siguiente = None
       self.anterior = None