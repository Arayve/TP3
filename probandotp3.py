from pila import Cola

from pila import Pila

import argparse

LIMITE_DE_BYTE = 256

def abc(pila, cola):

    cola_aux = Cola()

    pila_aux = Pila()

    '''while not pila.esta_vacia() :

        a = pila.desapilar()

        print(a," ",end="")

        print()

        pila_aux.apilar(a)

    while not pila_aux.esta_vacia() :

        a = pila_aux.desapilar()

        pila.apilar(a)'''

    while not cola.esta_vacia() :

        a = cola.desencolar()

        print(a," ",end="-")

        cola_aux.encolar(a)
    
    print()

    while not cola_aux.esta_vacia() :

        a = cola_aux.desencolar()

        cola.encolar(a)


def debug(cadena, i, mensaje):

    '''Recibe la cadena y el indice a evaluar.
       Imprime en pantalla un rango de 100 
       caracteres de la cadena y una flecha 
       en el caracter a evaluar'''

    print()

    print(mensaje)

    rango = (i // 100)  * 100

    print(cadena[rango:(rango +100)])

    print(" " * (i  % 100) + "^")

    input()

def ejecutar(cadena, modo_debug):

    mensaje = ""

    pila = Pila()

    cola = Cola()

    cola.encolar(0)

    mensaje = ""

    funciones = {"\\" : a, "/" : a ,"!" : b, "=" : b, "-" : c , "_" : c, "*" : d}

    i = 0

    while i < len(cadena) :

        elemento = cadena[i]

        if modo_debug:
            
            debug(cadena, i, mensaje)

        if not elemento in funciones:

            continue

        i, mensaje = funciones[elemento](elemento, i, cola, pila, mensaje)

def a(elemento, i, cola, pila, mensaje):

    pila_aux = Pila()

    if elemento == "/":

        anterior = i 

        if not pila.esta_vacia() :

            if pila.ver_tope() == i :

                pila.desapilar()

        i = pila.desapilar()

        pila.apilar(anterior)

    else :

        if cola.ver_primero() == 0 :

            i = pila.desapilar() + 1

        else:

            i += 1

    return i, mensaje

def b(elemento, i, cola, pila, mensaje):

    if elemento == "!" : 

        cola.encolar(0)
            
    elif elemento == "=":

        dato = cola.desencolar()

        cola.encolar(dato)

    return i + 1, mensaje

def c(elemento, i, cola, pila, mensaje):

    dato = cola.ver_primero()

    dato = dato -1 if elemento == "-" else dato +1 
                
    dato = dato % LIMITE_DE_BYTE

    cola.cambiar_primero(dato)

    return i + 1, mensaje

def d(elemento, i, cola, pila, mensaje):
    
    dato = cola.desencolar()

    letra = chr(dato)

    mensaje += letra

    print(letra, end = "")
                
    cola.encolar(dato)
            
    return i + 1, mensaje

            
def main():

    '''funcion principal, recibe por parametro
       el nombre del archivo sceql, lo abre y 
       lo guarda en una cadena.
       Acepta el modo DEBUG "-d" o "--debug", 
       en ese caso, imprime en pantalla un fragmento 
       del codigo fuente con una flecha en el caracter
       a evaluar '''
    
    parser = argparse.ArgumentParser(description='Interprete de codigo SCEQL')

    parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')

    parser.add_argument('-d', '--debug', action='store_true', help='modo debug')

    args = parser.parse_args()

    nombre_archivo = args.archivo

    modo_debug = args.debug

    cadena = []
    
    try:

        with open(nombre_archivo) as archivo :
        
            for linea in archivo:
            
                linea = linea.rstrip("\n")
        
                cadena.append(linea)
            
        cadena = "".join(cadena)

        ejecutar(cadena, modo_debug)

    except IOError:

        print("No se encuentra o no se permite abrir el archivo.")
    
main()
