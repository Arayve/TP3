import sys #https://sites.google.com/site/cursodepython/modulo-sys
#import argparse https://rctorr.wordpress.com/2014/01/16/procesando-parametros-en-la-linea-de-comando-en-python/ , lo vamos a usar despues para verificar

nombre_de_programa=sys.argv

cadena = " ________________________________________________________________________*_____________________________*_______**___*!=____________________________________________*=------------*________*=--------*=___*=------*=--------*_*!==__________*"

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

    def sceql (self, cadena):
        
        if self.esta_vacia():
            
            self.prim = _Nodo(0)
    
        aux = Cola()
    
        for caracter in cadena:
        
            if caracter == "!" :
            
                self.encolar(0)
            
            elif caracter == "=":
            
                byte = self.desencolar()
        
                self.encolar(byte)
            
            elif caracter == "-":
                
                dato = self.prim.dato - 1
                
                if dato == -1 :
                    
                    dato = 127
                
                self.prim.dato = dato
            
            elif caracter == "_" :
                
                dato = self.prim.dato + 1
                
                if dato == 128 :
                    
                    dato = 1
                    
                self.prim.dato = dato
            
            elif caracter == "*":
                
                dato = self.desencolar()
              
                print(chr(dato), end="")
                
                self.encolar(dato)
                
            elif caracter == "\\":
                
                if self.prim.dato == 0 :
                    
                    while self.prim.dato != "/" :
                        
                        dato = self.desencolar()
                        
                        aux.encolar()
                        
            elif caracter == "/":
                
                aux.sceql()
            
            
                