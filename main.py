from arbol import arbol_rojonegro
from turtle import *

def agregar_elemento(arbol, elemento):
    arbol = insertar_elemento(arbol, elemento)
    if arbol.rojo:
        arbol.rojo = False
    return arbol

def dar_minimo(arbol):
    
    if arbol.hijo_izquierdo is None:
        return arbol
    else:
        return dar_minimo(arbol.hijo_izquierdo)

def dar_maximo(arbol):
    
    if arbol.hijo_derecho is None:
        return arbol
    else:
        return dar_maximo(arbol.hijo_derecho)

def rotacion_izquierda(arbol):
    x = arbol.hijo_derecho
    arbol.hijo_derecho = x.hijo_izquierdo
    x.hijo_izquierdo = arbol
    x.rojo = arbol.rojo
    arbol.rojo = True
    #x.hijo_izquierdo.rojo = True
    return x 

def rotacion_derecha(arbol):
    x = arbol.hijo_izquierdo
    arbol.hijo_izquierdo = x.hijo_derecho
    x.hijo_derecho = arbol
    x.rojo = arbol.rojo
    arbol.rojo = True
    return x 



def invertir_colores(arbol):
    arbol.rojo = not arbol.rojo
    arbol.hijo_izquierdo.rojo = not arbol.hijo_izquierdo.rojo
    arbol.hijo_derecho.rojo = not arbol.hijo_derecho.rojo
    return arbol

def es_rojo(arbol):
    if arbol is None or not arbol.rojo:
        return False
    return True

def desplazamientoRojoIzquierdo(arbol):
    invertir_colores(arbol)
    if es_rojo(arbol.hijo_derecho.hijo_izquierdo):
        arbol.hijo_derecho = rotacion_derecha(arbol.hijo_derecho)
        arbol = rotacion_izquierda(arbol)
        invertir_colores(arbol)
    return arbol

def desplazamientoRojoDerecho(arbol):
    invertir_colores(arbol)
    if es_rojo(arbol.hijo_izquierdo.hijo_izquierdo):
        arbol = rotacion_derecha(arbol)
        invertir_colores(arbol)
    return arbol

def balancear(arbol):

    if es_rojo(arbol.hijo_derecho) and not es_rojo(arbol.hijo_izquierdo):
        arbol = rotacion_izquierda(arbol)
    
    if es_rojo(arbol.hijo_izquierdo) and es_rojo(arbol.hijo_izquierdo.hijo_izquierdo):
        arbol = rotacion_derecha(arbol)

    if es_rojo(arbol.hijo_izquierdo) and es_rojo(arbol.hijo_derecho):
        arbol = invertir_colores(arbol)

    return arbol

def eliminarMinimoNodo(arbol):
    if arbol.hijo_izquierdo is None:
        return None
    if not es_rojo(arbol.hijo_izquierdo) and not es_rojo(arbol.hijo_izquierdo.hijo_izquierdo):
        arbol = desplazamientoRojoIzquierdo(arbol)
    arbol.hijo_izquierdo = eliminarMinimoNodo(arbol.hijo_izquierdo)
    return balancear(arbol)

def eliminarMinimo(arbol):
    arbol = eliminarMinimoNodo(arbol)
    arbol.rojo = False
    return arbol

def eliminarMaximoNodo(arbol):
    
    if es_rojo(arbol.hijo_izquierdo):
        arbol = rotacion_derecha(arbol)
    if arbol.hijo_derecho is None:
        return None    
    if not es_rojo(arbol.hijo_derecho) and not es_rojo(arbol.hijo_derecho.hijo_izquierdo):
        arbol = desplazamientoRojoDerecho(arbol)   
    arbol.hijo_derecho = eliminarMaximoNodo(arbol.hijo_derecho)
    return balancear(arbol)

def eliminarMaximo(arbol):
    arbol = eliminarMaximoNodo(arbol)
    arbol.rojo = False
    return arbol

def eliminarNodo(arbol, llave):
    print(arbol.elemento)
    if llave < arbol.elemento:
        if not es_rojo(arbol.hijo_izquierdo) and not es_rojo(arbol.hijo_izquierdo.hijo_izquierdo):
            arbol = desplazamientoRojoIzquierdo(arbol)
        print("HERE-menor")
        arbol.hijo_izquierdo = eliminarNodo(arbol.hijo_izquierdo, llave)
    else:
        if es_rojo(arbol.hijo_izquierdo):
            
            arbol = rotacion_derecha(arbol)
        if arbol.elemento == llave and arbol.hijo_derecho is None:
            return None
        if not es_rojo(arbol.hijo_derecho) and not es_rojo(arbol.hijo_derecho.hijo_izquierdo):
            arbol = desplazamientoRojoDerecho(arbol)
            print(arbol)
        if llave == arbol.elemento:
            arbol.elemento = dar_minimo(arbol.hijo_derecho).elemento
            arbol.hijo_derecho = eliminarMinimoNodo(arbol.hijo_derecho)
        else:
            arbol.hijo_derecho = eliminarNodo(arbol.hijo_derecho, llave)

    return balancear(arbol)

def eliminarElemento(arbol, llave):
    arbol = eliminarNodo(arbol, llave)
    arbol.rojo = False
    return arbol

def insertar_elemento( arbol, elemento)->None:
    if arbol is None:
        arbol = arbol_rojonegro(elemento, None)
    elif elemento < arbol.elemento:
        arbol.hijo_izquierdo = insertar_elemento(arbol.hijo_izquierdo, elemento)
    else:
        arbol.hijo_derecho = insertar_elemento(arbol.hijo_derecho, elemento)


    arbol = balancear(arbol)

    return arbol

def dar_altura(arbol)->None:
    
    if arbol is None:
        return 0
    return 1 + max(dar_altura(arbol.hijo_izquierdo), dar_altura(arbol.hijo_derecho))




def pintar_nodo(arbol, x, y, xshift=150, yshift=70, nivel=1):
    if arbol is not None:
              
        xshift/=nivel
        
        penup()
        goto(x,y)
        pendown()

        color('black')
        if arbol.rojo:
            fillcolor('red')
        else:
            fillcolor('Black')
        begin_fill()
        circle(10)
        end_fill()       
        
        penup()
        goto(x,y)
        pendown()

        color('white')
        write(arbol.elemento, font=('Arial',8,'bold'), align='center')

        if es_rojo(arbol.hijo_izquierdo):
            color('red')
        else:
            color('black')

        goto(x-xshift, y-yshift)
        pintar_nodo(arbol.hijo_izquierdo, x-xshift, y-yshift, nivel=nivel+3)

        penup()
        goto(x,y)
        pendown()

        if es_rojo(arbol.hijo_derecho):
            color('red')
        else:
            color('black')
        
        goto(x+xshift, y-yshift)
        pintar_nodo(arbol.hijo_derecho, x+xshift, y-yshift, nivel=nivel+3)
        
def pintar_arbol(arbol):
    hideturtle()
    tracer(0, 0) 
    setup(700, dar_altura(arbol)*100)
    pintar_nodo(arbol, 0, dar_altura(arbol)*40)
    penup()
    goto(0,0)
    pendown()
    exitonclick()


if __name__=='__main__':
    arbol = None

    arbol = agregar_elemento(arbol, 'A')
    
    arbol = agregar_elemento(arbol, 'E')
    arbol = agregar_elemento(arbol, 'F')
    arbol = agregar_elemento(arbol, 'G')
    arbol = agregar_elemento(arbol, 'L')
    arbol = agregar_elemento(arbol, 'M')
    arbol = agregar_elemento(arbol, 'O')
    arbol = agregar_elemento(arbol, 'R')
    arbol = agregar_elemento(arbol, 'X')
    arbol = agregar_elemento(arbol, 'Z')
    arbol = agregar_elemento(arbol, 'P')
    arbol = agregar_elemento(arbol, 'D')
    #arbol = eliminarElemento(arbol, "F")
    #arbol = desplazamientoRojoDerecho(arbol)
    pintar_arbol(arbol)
