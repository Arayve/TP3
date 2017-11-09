from cola import Cola


def sceql(cadena):

    camino = {}
    
    barras = []
    
    for i in range(len(cadena)):
        
        c = cadena[i]
        
        if c == "\\":
            
            barras.append(i)

        elif c == "/":

            ultima_barra = barras.pop()
            
            camino[ultima_barra] = i
            
def recorrer(cadena):
    
    camino = sceql(cadena)
    
    cola = Cola()
    
    cola.encolar(0)
    
    i = 0
        
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

            a = cola.ver_tope()
                
            dato = (a - 1) % 128
                
            cola.cambiar_primero(dato)
            
            i += 1
            
        elif caracter == "_" :

            a = cola.ver_tope()
                
            dato = (a - 1) % 128
                
            cola.cambiar_primero(dato)
            
            i += 1
            
        elif caracter == "*" :

            dato = cola.desencolar()
              
            letra = chr(dato)  
            
            print(letra , end="")
                
            cola.encolar(dato)
            
            i += 1
                
        elif caracter == "/":

            if not cola.ver_tope():
                 
                continue
             
        elif caracter == "\\":
            
            i += 1
        else:
            
            i += 1
                 
recorrer(cadena)