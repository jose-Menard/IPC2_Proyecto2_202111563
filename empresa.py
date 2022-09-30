from listaDoblePA import ListaDoblePA
from listaDobleT import ListaDobleT

class Empresa:
    def __init__(self, codigo = None, nombre = None, abreviatura = None) -> None:
       self.codigo = codigo
       self.nombre = nombre
       self.abreviatura = abreviatura
       self.puntoAtencion=ListaDoblePA()
       self.transaccion=ListaDobleT()
       
       self.siguiente = None
       self.anterior = None