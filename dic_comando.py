
def funcion_del_comando_exclamacion(cola,i):
    cola.encolar(0)    
    i+=1
    return i
def funcion_del_comando_igual(cola,i):    
    dato = cola.desencolar()
    cola.encolar(dato)    
    i += 1
    return i
def funcion_del_comando_guion(cola,i,mensaje):        
    dato = cola.ver_frente() - 1   
    dato = dato % 256   
    cola.cambiar_primero(dato)    
    i += 1
    return i
def funcion_del_comando_guion_bajo(cola,i):           
    dato = cola.ver_frente() + 1        
    dato = dato % 256  
    cola.cambiar_primero(dato)        
    returni+= 1
def funcion_del_comando_asterisco(cola,i,mensaje):
    dato = cola.desencolar()     
    letra = chr(dato)      
    mensaje += letra
    print(letra, end = "")        
    cola.encolar(dato)         
    i+= 1
    return i , mensaje

def funcion_del_comando_barra(cola,i,camino_2):
    i = camino_2[i]
    return i
def funcion_del_comando_barra_invertida(cola,i,camino_1):
    i = i +1 if cola.ver_frente() != 0 else camino_1[i] + 1
    return i 


dic_comando={ 
            "!":funcion_del_comando_exclamacion,
            "=":funcion_del_comando_igual,
            "-":funcion_del_comando_guion,
            "_":funcion_del_comando_guion_bajo,
            "*":funcion_del_comando_asterisco,
            "/":funcion_del_comando_barra,
            "\\":funcion_del_comando_barra_invertida}





print(dic_comando)

