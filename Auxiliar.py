from cola import Cola

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
            
def recorrer(cadena):
    
    camino_1, camino_2 = sceql(cadena)
    
    archivo = open("archivo.txt", "w")
    
    cola = Cola()
    
    cola.encolar(0)
    
    i = 0
    lista = []
    while i < len(cadena):
        
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
            
            dato = dato % 128
            
            cola.cambiar_primero(dato)
            
            i += 1
            
        elif caracter == "_" :
                
            dato = cola.ver_tope() + 1
                
            dato = dato % 128
            
            cola.cambiar_primero(dato)
            
            i += 1
            
        elif caracter == "*" :

            dato = cola.desencolar()
            
            letra = chr(dato)  
            
            archivo.write(letra)
                
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
            
    archivo.close
    
def main():
    
    cadena = []
    
    with open("botellas.py") as archivo :
        
        for linea in archivo:
            
            linea = linea.rstrip("\n")
        
            cadena.append(linea)
            
    cadena = "".join(cadena)
    
    recorrer(cadena)
    
main()