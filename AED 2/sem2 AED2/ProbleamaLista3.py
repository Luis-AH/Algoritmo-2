import random

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.sig=None

class ListaSimple:
    def __init__(self):
        self.cabecera=None

    def agregarPorInicio(self,dato):
        nuevo=Nodo(dato)
        nuevo.sig=self.cabecera
        self.cabecera=nuevo

    def Mostrar(self):
        p=self.cabecera

        while(p):
            print(p.dato,end=" ")
            p=p.sig
    
    def buscar(self,datoBuscado):
        p=self.cabecera
        while(p):
            if(datoBuscado==p.dato):
                return p 
            p=p.sig
        return

def ingresarAle():
    for i in range(10):
        lista.agregarPorInicio(random.randint(10,50))


lista=ListaSimple()
ingresarAle()
