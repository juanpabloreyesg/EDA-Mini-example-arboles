from dataclasses import dataclass, field
from typing import List

@dataclass(repr=True)
class arbol_binario:

    elemento: int = None
    hijo_izquierdo: List['arbol_binario']= None
    hijo_derecho: List['arbol_binario']= None

    def agregar_elemento(self, padre, elemento)->None:
        if padre is None:
            self.elemento = elemento
        elif padre == self.elemento:
            if self.hijo_izquierdo is None:
                self.hijo_izquierdo = arbol_binario(elemento)
            elif self.hijo_derecho is None:
                self.hijo_derecho = arbol_binario(elemento)
        else:
            if self.hijo_izquierdo is not None:
                self.hijo_izquierdo.agregar_elemento(padre, elemento)
            if self.hijo_derecho is not None:
                self.hijo_derecho.agregar_elemento(padre, elemento)

@dataclass(repr=True)
class arbol_nario:

    elemento: int = None
    hijos: list = field(default_factory=list) 

    def agregar_elemento(self, padre, elemento)->None:
        if padre is None:
            self.elemento = elemento
        elif padre == self.elemento:
            self.hijos.append(arbol_nario(elemento))
        else:
            for hijo in self.hijos:
                hijo.agregar_elemento(padre, elemento)




@dataclass(repr=True)
class arbol_rojonegro:    

    elemento: int = None

    hijo_izquierdo: List['arbol_rojonegro']= None
    hijo_derecho: List['arbol_rojonegro']= None
    rojo: bool = True

    