from cola import Cola

from pila import Pila

import argparse

LIMITE_DE_BYTE = 256

def obt_pos_barras(cadena):

    '''Recibe en forma de cadena el codigo fuente
       de un programa/funcion en lenguaje SCEQL y
       devuelve dos diccionarios. Uno con la posicion
       de la "\" como clave y la posicion de "/" 
       correspondiente como valor y el otro inverso.'''

    camino_1 = {}
    
    camino_2 = {}
    
    barras = Pila()
    
    for i in range(len(cadena)):
        
        caracter = cadena[i]
    
        if caracter == "\\":

            barras.apilar(i)

        elif caracter == "/":

            ultima_barra = barras.desapilar()
            
            camino_1[ultima_barra] = i
            
            camino_2[i] = ultima_barra

    if not barras.esta_vacia():

        raise ValueError()
    
    return camino_1, camino_2
            


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

    '''Recibe en forma de cadena el codigo fuente
       de un programa/funcion en lenguaje SCEQL y
       lo interpreta.'''

    mensaje = ""

    camino_1, camino_2 = obt_pos_barras(cadena)

    cola = Cola()

    cola.encolar(0)

    mensaje = ""

    funciones = {"\\" : _barras, "/" : _barras ,"!" : _igual_admiracion, "=" : _igual_admiracion, "-" : _guiones , "_" : _guiones, "*" : _asterisco}

    i = 0

    while i < len(cadena):

        if modo_debug:
            
            debug(cadena, i, mensaje)

        if not cadena[i] in funciones:

            i += 1

            continue

        i, mensaje = funciones[cadena[i]](cadena[i], i, cola ,camino_1 , camino_2 , mensaje)

def _barras(elemento, i, cola, camino_1, camino_2 , mensaje):

    '''Recibe un elemento, una posicion, una cola,
    dos diccionarios y un mensaje.
    dependiendo de las condiciones de la cola, modifica
    la posiciom
    '''

    if elemento == "\\":

        if cola.ver_primero() == 0 :

            return camino_1[i] +1, mensaje

        return i + 1, mensaje

    return camino_2[i], mensaje

def _igual_admiracion(elemento, i, cola, camino_1, camino_2 , mensaje):

    '''Recibe un elemento, una posicion, una cola,
    dos diccionarios y un mensaje.
    Dependiendo del elemento, modifica la cola
    '''

    if elemento == "!" : 

        cola.encolar(0)
            
    elif elemento == "=":

        dato = cola.desencolar()

        cola.encolar(dato)

    return i + 1, mensaje

def _guiones(elemento, i, cola, camino_1, camino_2 , mensaje):

    '''Recibe un elemento, una posicion, una cola,
    dos diccionarios y un mensaje.
    deependiendo del elemento, modifica la cola
    '''

    dato = cola.ver_primero()

    dato = dato -1 if elemento == "-" else dato +1 
                
    dato = dato % LIMITE_DE_BYTE

    cola.cambiar_primero(dato)

    return i + 1, mensaje

def _asterisco(elemento, i, cola, camino_1, camino_2 , mensaje):
    
    '''Recibe un elemento, una posicion, una cola,
    dos diccionarios y un mensaje.
    Imprime en pantalla el primer elemento de la cola
    paso usando la tabla ASCII
    '''

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

    except ValueError:

        print("Error. Deben haber igual cantidad de '\\' que '/'.")

    except IndexError:

        print("Error. Deben haber igual cantidad de '\\' que '/'.")
    
main()
