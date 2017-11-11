from cola import Cola

import argparse

def sceql(cadena):

    camino_1 = {}
    
    camino_2 = {}
    
    barras = []
    
    for i in range(len(cadena)):
        
        c = cadena[i]
    
        if c == "\\":

            barras.append(i)

        elif c == "/":

            ultima_barra = barras.pop()
            
            camino_1[ultima_barra] = i
            
            camino_2[i] = ultima_barra
    
    return camino_1, camino_2
            
def recorrer(cadena, modo_debug):
    
    camino_1, camino_2 = sceql(cadena)
    
    cola = Cola()
    
    cola.encolar(0)
    
    i = 0

    mensaje = ""

    while i < len(cadena):

        if modo_debug :

            print(mensaje)

            print(cadena[i:i+60])

            input("^")

        caracter = cadena[i]
        

        if caracter == "!" : 

            cola.encolar(0)
            
            i += 1
            
        elif caracter == "=":

            dato = cola.desencolar()

            cola.encolar(dato)
        
            i += 1
            
        elif caracter == "-":
                
            dato = cola.ver_tope() - 1
            
            dato = dato % 256
            
            cola.cambiar_primero(dato)
            
            i += 1
            
        elif caracter == "_" :
                
            dato = cola.ver_tope() + 1
                
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
            
            if cola.ver_tope() != 0:
                
                i += 1
                
            else:
                          
                i = camino_1[i] + 1
                
        else:
            
            i += 1
            
def main():
    
    parser = argparse.ArgumentParser(description='Interprete de codigo SCEQL')

    parser.add_argument('archivo', metavar='archivo', help='archivo con codigo a interpretar')

    parser.add_argument('-d', '--debug', action='store_true', help='modo debug')

    args = parser.parse_args()

    nombre_archivo = args.archivo

    modo_debug = args.debug

    cadena = []
    
    with open(nombre_archivo) as archivo :
        
        for linea in archivo:
            
            linea = linea.rstrip("\n")
        
            cadena.append(linea)
            
    cadena = "".join(cadena)
    
    recorrer(cadena, modo_debug)
    
main() 