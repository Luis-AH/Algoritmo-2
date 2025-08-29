#Crea una lista de 10 números aleatorios
#Agregar por inicio, mostrar, sumar todos, contar la cant de pares, buscar un numero y si existe, modificarlo

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
    
    def ContarPar(self):
        p=self.cabecera
        par=0
        while(p):
            if(p.dato%2==0):
                par+=1
            p=p.sig
        return par
    
    def Sumar(self):
        p=self.cabecera
        sum=0
        while(p):
            if(p.dato%2==0):
                sum+=p.dato
            p=p.sig
        return sum
    
    def Eliminar():
        datoBuscado=int(input("\n¿Cuál es el dato que busca?: "))
        p=lista.buscar(datoBuscado)
        if(p==None):
            print("dato no encontrado")
    
        else:
             print("encontrado")
             p.dato=None
    

def ingresarAle():
    for i in range(10):
        lista.agregarPorInicio(random.randint(10,50))

def procesoBuscarMod():
    datoBuscado=int(input("\n¿Cuál es el dato que busca?: "))
    p=lista.buscar(datoBuscado)
    if(p==None):
        print("dato no encontrado")
    
    else:
        print("encontrado")
        p.dato=int(input("ingresa el nuevo dato: "))

#segundo metodo
"""
def Modificar(self,nn,p):
    p.dato=nn
"""


        


lista=ListaSimple()
ingresarAle()
lista.Mostrar()
print("\nla cantidad de números pares es: ",lista.ContarPar())
print("\nla suma total es: ",lista.Sumar())
procesoBuscarMod()
lista.Mostrar()
