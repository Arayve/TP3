
LIMITE_DE_BYTE = 256

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


dic_funciones = {"\\" : _barras, "/" : _barras ,"!" : _igual_admiracion, "=" : _igual_admiracion, "-" : _guiones , "_" : _guiones, "*" : _asterisco}
