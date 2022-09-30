class TransaNueva:
    def __init__(self, idtrans = None, cantidad = None) -> None:
       self.idtrans = idtrans
       self.cantidad=cantidad

       self.siguiente = None
       self.anterior = None