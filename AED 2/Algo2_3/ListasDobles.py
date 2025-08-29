import random

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.sig=None
        self.ant=None

class ListaDoble:
    def __init__(self):
        self.inicio=None #cabecera
        self.fin=None #ultimo 

    def agregarInicio(self,dato):
        nuevo=Nodo(dato)

        if self.inicio is None: #esta vacia
            self.inicio=nuevo
            self.fin=nuevo
        
        else:
            nuevo.sig=self.inicio
            self.inicio.ant=nuevo
            self.inicio=nuevo

    def agregarFinal(self,dato):
        nuevo=Nodo(dato)

        if self.inicio is None: #esta vacia
            self.inicio=nuevo
            self.fin=nuevo
        
        else:
            self.fin.sig=nuevo
            nuevo.ant=self.fin
            self.fin=nuevo

    def mostrarDatosAvanzando(self):
        p=self.inicio

        while p:
            print(p.dato,end=" ")
            p=p.sig

    def mostrarDatosRetroceso(self):
        p=self.fin
        while p:
            print(p.dato,end=" ")
            p=p.ant

    def Buscar(self,bus):
        p=self.inicio

        while p:
            if(p.dato==bus):
                return p
            p=p.sig

        return None
            
            
#___________________

listD=ListaDoble()


print("agregando por el inicio")
for i in range (7):
    nAle=random.randint(10,50)
    listD.agregarInicio(nAle)

#print("agregando por el final")
#for i in range (7):
    #nAle=random.randint(10,50)
    #listD.agregarFinal(nAle)

print("\nMostrando lista avanzando...\n ")

listD.mostrarDatosAvanzando()


print("\nMostrando lista retrocediendo...\n ")

listD.mostrarDatosRetroceso()

print("\nproceso de busqueda...")
bus=int(input("Ingresa el dato a buscar: "))

p=listD.Buscar(bus)
if p is None:
    print("\nNo encontrado")

else:
    print("\nEncontrado")

    try: 
        print("Número anterior:",p.ant.dato)

    except AttributeError:
        print("Número anterior: Nulo")

    try:    
        print("Número siguiente:",p.sig.dato)
    
    except AttributeError:
        print("Número siguiente: Nulo")
    
    