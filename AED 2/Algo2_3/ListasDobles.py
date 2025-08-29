class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.ant = None
        self.sig = None

class ListaDobleEnlazada:
    def __init__(self):
        self.inicio = None  # Cabeza
        self.fin = None     # Cola

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.inicio is None:
            self.inicio = self.fin = nuevo
        else:
            self.fin.sig = nuevo
            nuevo.ant = self.fin
            self.fin = nuevo

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.inicio is None:
            self.inicio = self.fin = nuevo
        else:
            nuevo.sig = self.inicio
            self.inicio.ant = nuevo
            self.inicio = nuevo

    def mostrar_adelante(self):
        p = self.inicio
        while p:
            print(p.dato, end="  ")
            p = p.sig
 
    def mostrar_atras(self):
        p = self.fin
        while p:
            print(p.dato, end="  ")
            p = p.ant
   

    def eliminar(self, dato):
        p = self.inicio    
        while p:
            if p.dato == dato:
                if p.ant: 
                    p.ant.sig = p.sig
                else:
                    self.inicio = p.sig  
                if p.sig:   
                    p.sig.ant = p.ant
                else:
                    self.fin = p.ant  
                return True
            p = p.sig
        return False


#---------------------
import random

listaD=ListaDobleEnlazada()
print("lista insertada por el inicio")
for i in range (5):
     ale=random.randint(10,50)
     listaD.insertar_al_inicio(ale)

listaD.mostrar_adelante()  

#listaD.mostrar_atras()  #comentado para probar el otro mostrar, descomentar si desean probar

dato=int(input("\nleer el dato a eliminar:"))
listaD.eliminar(dato)

listaD.mostrar_adelante()  
