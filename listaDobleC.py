from clientes import Clientes

class ListaDobleC:
    def __init__(self) -> None:
        self.raiz = Clientes()
        self.ultimo = Clientes()
    
    def append(self, nuevoCliente):
        if self.raiz.dpi is None:
            self.raiz = nuevoCliente
            self.ultimo = nuevoCliente
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoCliente
            nuevoCliente.anterior = self.raiz
            self.ultimo = nuevoCliente
        else:
            self.ultimo.siguiente = nuevoCliente
            nuevoCliente.anterior = self.ultimo
            self.ultimo = nuevoCliente
    
    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.dpi is not None:
                cadena += "(" + nodoAux.dpi + " , " + nodoAux.nombre + " )"
                if nodoAux.siguiente is not None:
                    if nodoAux.dpi!=nodoAux.siguiente.dpi:
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
            if i.dpi==dato:
                print(dato)
                return True
            i=i.siguiente
        return False
    
    def buscarByCodigo(self, codigo):
        nodoAux=self.raiz
        
        while nodoAux.dpi!=codigo:
            if nodoAux.siguiente is not None:
                nodoAux=nodoAux.siguiente
            else:
                return None
        
        return nodoAux