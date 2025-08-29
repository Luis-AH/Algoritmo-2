#Crear una lista enlazada, almacenar los datos  (numéricos)

class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.sig=None

#------------------------------

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


lista=ListaSimple()
lista.agregarPorInicio(12)
lista.agregarPorInicio(15)
lista.agregarPorInicio(23)
lista.agregarPorInicio(30)
lista.Mostrar()