
def funcion_de_comando_no_existente(cola,i,mensaje,camino_1,camino_2):
    i += 1 
    return i,mensaje
def funcion_del_comando_exclamacion(cola,i,mensaje,camino_1,camino_2):
    cola.encolar(0) 
    i += 1   
    return i,mensaje
def funcion_del_comando_igual(cola,i,mensaje,camino_1,camino_2):    
    dato = cola.desencolar()
    cola.encolar(dato)
    i += 1    
    return i,mensaje
def funcion_del_comando_guion(cola,i,mensaje,camino_1,camino_2):        
    dato = cola.ver_frente() - 1   
    dato = dato % 256   
    cola.cambiar_primero(dato)
    i += 1    
    return i,mensaje
def funcion_del_comando_guion_bajo(cola,i,mensaje,camino_1,camino_2):           
    dato = cola.ver_frente() + 1        
    dato = dato % 256  
    cola.cambiar_primero(dato)
    i += 1        
    return i,mensaje
def funcion_del_comando_asterisco(cola,i,mensaje,camino_1,camino_2):
    dato = cola.desencolar()     
    letra = chr(dato)      
    mensaje += letra
    print(letra, end = "")        
    cola.encolar(dato)         
    i += 1
    return i,mensaje

def funcion_del_comando_barra(cola,i,mensaje,camino_1,camino_2):
    i = camino_2[i]
    return i,mensaje
def funcion_del_comando_barra_invertida(cola,i,mensaje,camino_1,camino_2):
    i = i +1 if cola.ver_frente() != 0 else camino_1[i] + 1
    return i,mensaje

comandos={ 
            "!":funcion_del_comando_exclamacion,
            "=":funcion_del_comando_igual,
            "-":funcion_del_comando_guion,
            "_":funcion_del_comando_guion_bajo,
            "*":funcion_del_comando_asterisco,
            "/":funcion_del_comando_barra,
            "\\":funcion_del_comando_barra_invertida}

