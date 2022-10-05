from empresa import Empresa
class ListaDoble:
    def __init__(self) -> None:
        self.raiz = Empresa()
        self.ultimo = Empresa()

    def append(self, nuevaEmpresa):
        if self.raiz.codigo is None:
            self.raiz = nuevaEmpresa
            self.ultimo = nuevaEmpresa
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevaEmpresa
            nuevaEmpresa.anterior = self.raiz
            self.ultimo = nuevaEmpresa
        else:
            self.ultimo.siguiente = nuevaEmpresa
            nuevaEmpresa.anterior = self.ultimo
            self.ultimo = nuevaEmpresa
    
    def print(self):
        nodoAux = self.raiz
        cadena = ''
        while True:
            if nodoAux.codigo is not None:
                cadena += "(" + nodoAux.codigo + " , " + nodoAux.nombre + " , " + nodoAux.abreviatura + ")"
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
    
    def iterar(self):
        actual=self.raiz

        while actual:
            codigo=actual.codigo
            actual=actual.siguiente
            yield codigo
    
    def buscarByCodigo(self, codigo):
        nodoAux=self.raiz
        
        while nodoAux.codigo!=codigo:
            if nodoAux.siguiente is not None:
                nodoAux=nodoAux.siguiente
            else:
                return None
        
        return nodoAux
    
    def search(self,dato):
        i=self.raiz
        while i:
            if i.codigo==dato:
                print(dato)
                return True
            i=i.siguiente
        return False
                

    