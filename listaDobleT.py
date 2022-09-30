from transacciones import Transacciones
import os

class ListaDobleT:
    def __init__(self) -> None:
        self.raiz = Transacciones()
        self.ultimo = Transacciones()
    
    def append(self, nuevaTransaccion):
        if self.raiz.codigo is None:
            self.raiz = nuevaTransaccion
            self.ultimo = nuevaTransaccion
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaTransaccion
            nuevaTransaccion.anterior = self.raiz
            self.ultimo = nuevaTransaccion
        else:
            self.ultimo.siguiente = nuevaTransaccion
            nuevaTransaccion.anterior = self.ultimo
            self.ultimo = nuevaTransaccion
    
    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.codigo is not None:
                cadena += "(" + nodoAux.codigo + " , " + nodoAux.nombre + " , " + nodoAux.minutos + ")"
                if nodoAux.siguiente is not None:
                    if nodoAux.codigo!=nodoAux.siguiente.codigo:
                        cadena += ""
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)  

