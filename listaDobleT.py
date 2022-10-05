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

    def search(self,dato):
        i=self.raiz
        while i:
            if i.codigo==dato:
                print(dato)
                return True
            i=i.siguiente
        return False
    
    def buscarByCodigo(self, codigo):
        nodoAux=self.raiz
        
        while nodoAux.codigo!=codigo:
            if nodoAux.siguiente is not None:
                nodoAux=nodoAux.siguiente
            else:
                return None
        
        return nodoAux

