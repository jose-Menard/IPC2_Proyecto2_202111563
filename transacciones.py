class Transacciones:
    def __init__(self, codigo = None, nombre = None, minutos = None) -> None:
       self.codigo = codigo
       self.nombre = nombre
       self.minutos = minutos
       
       self.siguiente = None
       self.anterior = None