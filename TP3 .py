import sys #https://sites.google.com/site/cursodepython/modulo-sys
#import argparse https://rctorr.wordpress.com/2014/01/16/procesando-parametros-en-la-linea-de-comando-en-python/ , lo vamos a usar despues para verificar

nombre_de_programa=sys.argv

class _Nodo:
    
    def __init__ (self, dato, prox= None):
        
        self.dato = dato
        
        self.prox = prox
        
class Cola:
    
    def __init__(self):
        
        self.primero = None
        
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