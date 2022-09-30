from transaNueva import TransaNueva

class ListaDobleTransa:
    def __init__(self) -> None:
        self.raiz = TransaNueva()
        self.ultimo = TransaNueva()
    
    def append(self, nuevaTransa):
        if self.raiz.idtrans is None:
            self.raiz = nuevaTransa
            self.ultimo = nuevaTransa
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaTransa
            nuevaTransa.anterior = self.raiz
            self.ultimo = nuevaTransa
        else:
            self.ultimo.siguiente = nuevaTransa
            nuevaTransa.anterior = self.ultimo
            self.ultimo = nuevaTransa
    
    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.idtrans is not None:
                cadena += "(" + nodoAux.idtrans + " , " + nodoAux.cantidad+")"
                if nodoAux.siguiente is not None:
                    if nodoAux.idtrans!=nodoAux.siguiente.idtrans:
                        cadena += ""
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)  