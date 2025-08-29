
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.sig=None

class ListaSimple:
    def __init__(self):
        self.cabecera=None

    def agregarPorFinal(self,dato):
        nuevo=Nodo(dato)
        if(self.cabecera==None): #si no hay nodo o lista vacia
            self.cabecera=nuevo
        else:
            p=self.cabecera
            while(p.sig is not None):
                p=p.sig
            p.sig=nuevo

    def Mostrar(self):
        p=self.cabecera

        while(p):
            print(p.dato,end=" ")
            p=p.sig #avanza al siguiente nodo
    
    def buscar(self,datoBuscado):
        p=self.cabecera
        while(p):
            if(datoBuscado==p.dato):
                return p 
            p=p.sig
        return
        


lista=ListaSimple()


def Ingresar():
    for i in range(5):
        num=int(input("Ingrese un número: "))
        lista.agregarPorFinal(num)

Ingresar()

def Listado():
    print("\nla  lista es la siguiente: ")
    print()
    lista.Mostrar()

def procesoBuscar():
    datoBuscado=int(input("\n¿Cuál es el dato que busca?: "))
    p=lista.buscar(datoBuscado)
    if(p==None):
        print("dato no encontrado")
    
    else:
        print("encontrado, el valor es: ",p.dato)

Listado()
procesoBuscar()