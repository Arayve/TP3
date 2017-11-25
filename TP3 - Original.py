from cola import Cola

from pila import Pila

from dic_comando import *

import argparse

def debug(cadena, i):

    '''Recibe la cadena y el indice a evaluar.
       Imprime en pantalla un rango de 100 
       caracteres de la cadena y una flecha 
       en el caracter a evaluar'''

    rango = (i // 100)  * 100

    print(cadena[rango:(rango +100)])

    print(" " * (i  % 100) + "^")



def sceql(cadena):

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
            


def recorrer(cadena, modo_debug):

    '''Recibe en forma de cadena el codigo fuente
       de un programa/funcion en lenguaje SCEQL y
       lo interpreta.
       De no haber "\" y "/" en iguales cantidades,
       levanta error '''
    
    camino_1, camino_2 = sceql(cadena)
    
    cola = Cola()
    
    cola.encolar(0)
    
    i = 0

    mensaje = ""

    while i < len(cadena):
        
        if modo_debug :

            print()

            print(mensaje)

            debug(cadena, i)

            input()

        caracter = cadena[i]
        

        if caracter == "!" : 

            cola.encolar(0)
            
            i += 1
            
        elif caracter == "=":

            dato = cola.desencolar()

            cola.encolar(dato)
        
            i += 1
            
        elif caracter == "-":
                
            dato = cola.ver_frente() - 1
            
            dato = dato % 256
            
            cola.cambiar_primero(dato)
            
            i += 1
            
        elif caracter == "_" :
                
            dato = cola.ver_frente() + 1
                
            dato = dato % 256
            
            cola.cambiar_primero(dato)
            
            i += 1
            
        elif caracter == "*" :

            dato = cola.desencolar()
            
            letra = chr(dato)  
            
            mensaje += letra

            print(letra, end = "")
                
            cola.encolar(dato)
            
            i += 1
                
        elif caracter == "/":
            
            i = camino_2[i]
             
        elif caracter == "\\":
            
            i = i +1 if cola.ver_frente() != 0 else camino_1[i] + 1
            
        else:
            
            i += 1


            
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

        recorrer(cadena, modo_debug)

    except ValueError:

        print("Error. Deben haber igual cantidad de '\\' que '/'.")

    except IndexError:

        print("Error. Deben haber igual cantidad de '\\' que '/'.")

    except IOError:

        print("No se encuentra o no se permite abrir el archivo.")
    
main() 