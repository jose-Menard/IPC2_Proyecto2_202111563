from configuracion import Configuracion

class ListaDobleConfi:
    def __init__(self) -> None:
        self.raiz = Configuracion()
        self.ultimo = Configuracion()
    
    def append(self, nuevaConfiguracion):
        if self.raiz.idC is None:
            self.raiz = nuevaConfiguracion
            self.ultimo = nuevaConfiguracion
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaConfiguracion
            nuevaConfiguracion.anterior = self.raiz
            self.ultimo = nuevaConfiguracion
        else:
            self.ultimo.siguiente = nuevaConfiguracion
            nuevaConfiguracion.anterior = self.ultimo
            self.ultimo = nuevaConfiguracion
    
    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.idC is not None:
                cadena += "(" + nodoAux.idC + " , " + nodoAux.idE + " , " + nodoAux.idP + ")"
                if nodoAux.siguiente is not None:
                    if nodoAux.idC!=nodoAux.siguiente.idC:
                        cadena += ""
                    nodoAux = nodoAux.siguiente
                    cadena += " -> "
                else:
                    break
            else:
                break
        
        print(cadena)  