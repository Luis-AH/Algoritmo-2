tam=int(input("cuántos atletas participaron: "))

at=[0]*tam

def Poblar():
    for i in range (tam):
     at[i]=int(input("el tiempo que tardó (seg.): "))

def Mostrar():
   for i in range (tam):
        print(at[i],end=" ")

def OrdenarB():
   for i in range (tam-1):
      for j in range(i+1,tam):
         if(at[i]>at[j]):
            #intercambiar
            aux=at[i]
            at[i]=at[j]
            at[j]=aux

Poblar()
print("Antes de ordenarlos\n")
Mostrar()
OrdenarB()
print("\nDespués de ordenarlos\n")
Mostrar()
