import random

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.sig=None

class ListaCircular:
    def __init__(self):
        self.inicio=None #cabecera

    def agregarInicio(self,dato):
        nuevo=Nodo(dato)

        if self.inicio is None: #esta vacia
            self.inicio=nuevo
            self.inicio.sig=self.inicio
        
        else:
            nuevo.sig=self.inicio
            self.inicio.sig=nuevo
            self.inicio=nuevo

    def mostrarDatosAvanzando(self):
        p=self.inicio

        while p:
            print(p.dato,end=" ")
            p=p.sig

           



listaC=ListaCircular()

n=int(input("número de datos:"))
for i in range (n):
    listaC.agregarInicio(random.randint(2,15))

listaC.mostrarDatosAvanzando()





