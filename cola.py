class _Nodo:
    
    def __init__ (self, dato, prox= None):
        
        self.dato = dato
        
        self.prox = prox
        
class Cola:
    
    def __init__(self):
        
        self.prim = None
        
        self.ultimo = None
        
    def encolar (self, dato):
        
        nodo = _Nodo(dato)
        
        if not self.prim:
            
            self.prim = nodo
            
        else:
            
            self.ultimo.prox = nodo
            
        self.ultimo = nodo
        
    def desencolar (self):
        
        nodo = self.prim
        
        dato = nodo.dato
        
        self.prim = nodo.prox
        
        return dato
    
    def esta_vacia (self):
        
        return self.prim is None
    
    def ver_primero(self):
        
        if not self.prim:
            
            raise ValueError()
        
        return self.prim.dato
