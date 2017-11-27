from Comandos import DIC_FUNCIONES

from cola import Cola

from pila import Pila

import argparse



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
            

def debug(cadena, i, mensaje,cola):
    '''Recibe la cadena y el indice a evaluar.
       Imprime en pantalla un rango de 100 
       caracteres de la cadena y una flecha 
       en el caracter a evaluar'''

    print()
    
    cola.imprimir_cola()
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


    i = 0

    while i < len(cadena):

        if modo_debug:
            
            debug(cadena, i, mensaje,cola)

        if not cadena[i] in DIC_FUNCIONES:

            i += 1

            continue

        i, mensaje = DIC_FUNCIONES[cadena[i]](cadena[i], i, cola ,camino_1 , camino_2 , mensaje)


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
