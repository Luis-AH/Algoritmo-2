
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class ListaCircular:
    def __init__(self):
        self.ult = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
     
        if self.ult is None:
            self.ult = nuevo
            self.ult.sig = self.ult
        else:
            nuevo.sig = self.ult.sig
            self.ult.sig = nuevo
            self.ult = nuevo

    def mostrar(self):
        if not self.ult:
            print("Lista vacía")
            return
        actual = self.ult.sig
        while True:
            print(actual.dato, end=" -> ")
            actual = actual.sig
            if actual == self.ult.sig:
                break
        print()

    def buscar(self, valor):
        if not self.ult:
            return False
        actual = self.ult.sig
        while True:
            if actual.dato == valor:
                return True
            actual = actual.sig
            if actual == self.ult.sig:
                break
        return False

    
#---------------------------------
import random

lista = ListaCircular()

for i in range (10):
    nAle=random.randint(10,50)
    lista.agregar(nAle)


lista.mostrar()

numB=int(input("Ingrese un número a buscar:"))
p=lista.buscar(numB)
if(p==None):
	print("NO se encuentra en lista...")
else:
	print("Encontrado!")




