class _Nodo:
    
    def __init__ (self, dato, prox= None):
        
        self.dato = dato
        
        self.prox = prox
            
#-----------------------------------------------------------------------------
class Sceql:

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

    def ejecutar(self,cadena):
        #Borre el encolar del nodo , no se por que encolas un cero al inciio
        if self.esta_vacia():
            
            self.prim = _Nodo(0)

        for caracter in cadena:
        
            if caracter == "!" : 
            
                self.encolar(0)
            
            elif caracter == "=":
            
                byte = self.desencolar()#si desencola algo vacio deberia hacer saltar un error especifico 
        
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



x=Sceql()
x.ejecutar(" ________________________________________________________________________*_____________________________*_______**___*!=____________________________________________*=------------*________*=--------*=___*=------*=--------*_*!==__________*")
