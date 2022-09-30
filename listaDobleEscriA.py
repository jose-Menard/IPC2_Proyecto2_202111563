from escriActivos import EscriActivos

class ListaDobleEscriA:
    def __init__(self) -> None:
        self.raiz = EscriActivos()
        self.ultimo = EscriActivos()
    
    def append(self, nuevoEscriA):
        if self.raiz.id is None:
            self.raiz = nuevoEscriA
            self.ultimo = nuevoEscriA
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoEscriA
            nuevoEscriA.anterior = self.raiz
            self.ultimo = nuevoEscriA
        else:
            self.ultimo.siguiente = nuevoEscriA
            nuevoEscriA.anterior = self.ultimo
            self.ultimo = nuevoEscriA
    
    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.id is not None:
                cadena += "(" + nodoAux.id + ")"
                if nodoAux.siguiente is not None:
                    if nodoAux.id!=nodoAux.siguiente.id:
                        cadena += ""
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)  