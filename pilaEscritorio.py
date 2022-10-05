from escritorios import Escritorios

class PilaEscritorio:
    def __init__(self) -> None:
        self.raiz = Escritorios()
       

    def append(self, codigo, identi, nombreEm,estado):
        escritorioso=Escritorios(codigo, identi, nombreEm,estado)

        if self.raiz:
            escritorioso.siguiente=self.raiz
            self.raiz=escritorioso
        else:
            self.raiz=escritorioso

    
    def delete(self):
        if not self.raiz:
            return False
        else:
            current=self.raiz
            self.raiz=self.raiz.siguiente
            return True
        return False
    
    def getFirst(self):
        primeroso= self.raiz.nombreE
        print(primeroso)
    
    def getLast(self):
        current=self.raiz
        while (current.siguiente):
            current=current.siguiente
        ultimoso=current.nombreE
        print(ultimoso)
    
    def printPila(self):
        nodoAux = self.raiz
        cadena = ''

        while True:
            if nodoAux.codigo is not None:
                cadena += "(" + nodoAux.codigo + " , " + nodoAux.identificacion + " , " + nodoAux.nombreE +" , " + nodoAux.estado+ ")"
                if nodoAux.siguiente is not None:
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