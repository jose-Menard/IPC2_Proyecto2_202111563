from pilaEscritorio import PilaEscritorio

class PuntoAtencion:
    def __init__(self, codigo = None, nombre = None, direccion = None) -> None:
       self.codigo = codigo
       self.nombre = nombre
       self.direccion = direccion
       self.escritorio=PilaEscritorio()
       
       self.siguiente = None
       self.anterior = None